#!/usr/bin/env python3
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

CONFIG_DIR = Path('/data/.openclaw/workspace/tmp/google-calendar')
CONFIG_FILE = CONFIG_DIR / 'credentials.json'
SCOPES = ['https://www.googleapis.com/auth/calendar']
REDIRECT_URI = 'http://localhost'
AUTH_URL = 'https://accounts.google.com/o/oauth2/v2/auth'
TOKEN_URL = 'https://oauth2.googleapis.com/token'


def load_config():
    if not CONFIG_FILE.exists():
        return {}
    return json.loads(CONFIG_FILE.read_text())


def save_config(data):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False))


def cmd_init(args):
    if len(args) != 2:
        print('Usage: google_calendar_oauth.py init <client_id> <client_secret>', file=sys.stderr)
        sys.exit(1)
    client_id, client_secret = args
    cfg = load_config()
    cfg.update({
        'client_id': client_id,
        'client_secret': client_secret,
        'calendar_id': cfg.get('calendar_id', 'primary'),
    })
    save_config(cfg)
    print(f'Saved credentials to {CONFIG_FILE}')


def cmd_auth_url(args):
    cfg = load_config()
    client_id = cfg.get('client_id')
    if not client_id:
        print('Missing client_id. Run init first.', file=sys.stderr)
        sys.exit(1)
    params = {
        'client_id': client_id,
        'redirect_uri': REDIRECT_URI,
        'response_type': 'code',
        'scope': ' '.join(SCOPES),
        'access_type': 'offline',
        'prompt': 'consent',
    }
    print(AUTH_URL + '?' + urllib.parse.urlencode(params))


def cmd_exchange(args):
    if len(args) != 1:
        print('Usage: google_calendar_oauth.py exchange <auth_code>', file=sys.stderr)
        sys.exit(1)
    code = args[0]
    cfg = load_config()
    client_id = cfg.get('client_id')
    client_secret = cfg.get('client_secret')
    if not client_id or not client_secret:
        print('Missing client_id/client_secret. Run init first.', file=sys.stderr)
        sys.exit(1)
    payload = urllib.parse.urlencode({
        'code': code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': REDIRECT_URI,
        'grant_type': 'authorization_code',
    }).encode()
    req = urllib.request.Request(TOKEN_URL, data=payload, method='POST')
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    with urllib.request.urlopen(req) as resp:
        data = json.load(resp)
    if 'refresh_token' not in data:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        print('No refresh_token returned. Try again with prompt=consent and a fresh authorization.', file=sys.stderr)
        sys.exit(1)
    cfg['refresh_token'] = data['refresh_token']
    cfg['last_token_response'] = data
    save_config(cfg)
    print('Refresh token saved.')


def refresh_access_token(cfg):
    payload = urllib.parse.urlencode({
        'client_id': cfg['client_id'],
        'client_secret': cfg['client_secret'],
        'refresh_token': cfg['refresh_token'],
        'grant_type': 'refresh_token',
    }).encode()
    req = urllib.request.Request(TOKEN_URL, data=payload, method='POST')
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)['access_token']


def cmd_test(_args):
    cfg = load_config()
    required = ['client_id', 'client_secret', 'refresh_token']
    missing = [k for k in required if not cfg.get(k)]
    if missing:
        print('Missing: ' + ', '.join(missing), file=sys.stderr)
        sys.exit(1)
    token = refresh_access_token(cfg)
    cal_id = urllib.parse.quote(cfg.get('calendar_id', 'primary'))
    url = f'https://www.googleapis.com/calendar/v3/calendars/{cal_id}/events?maxResults=3&singleEvents=true&orderBy=startTime'
    req = urllib.request.Request(url)
    req.add_header('Authorization', f'Bearer {token}')
    with urllib.request.urlopen(req) as resp:
        data = json.load(resp)
    print(json.dumps(data, indent=2, ensure_ascii=False))


def main():
    if len(sys.argv) < 2:
        print('Usage: google_calendar_oauth.py <init|auth-url|exchange|test> ...', file=sys.stderr)
        sys.exit(1)
    cmd = sys.argv[1]
    args = sys.argv[2:]
    if cmd == 'init':
        cmd_init(args)
    elif cmd == 'auth-url':
        cmd_auth_url(args)
    elif cmd == 'exchange':
        cmd_exchange(args)
    elif cmd == 'test':
        cmd_test(args)
    else:
        print(f'Unknown command: {cmd}', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
