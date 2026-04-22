# Google Calendar setup para TANQUE

## Qué queda preparado
- Script OAuth local: `scripts/google_calendar_oauth.py`
- Carpeta de credenciales: `tmp/google-calendar/credentials.json`
- Scope configurado: `https://www.googleapis.com/auth/calendar`

## Paso 1
Crea credenciales OAuth en Google Cloud:
- Tipo: **Desktop app**
- API: **Google Calendar API** habilitada

## Paso 2
Guarda `client_id` y `client_secret`:

```bash
python3 /data/.openclaw/workspace/scripts/google_calendar_oauth.py init '<CLIENT_ID>' '<CLIENT_SECRET>'
```

## Paso 3
Saca la URL de autorización:

```bash
python3 /data/.openclaw/workspace/scripts/google_calendar_oauth.py auth-url
```

Ábrela con la cuenta `tanqueoc@gmail.com`, acepta permisos y copia el valor `code` de la URL final.

## Paso 4
Intercambia el código por refresh token:

```bash
python3 /data/.openclaw/workspace/scripts/google_calendar_oauth.py exchange '<AUTH_CODE>'
```

## Paso 5
Prueba la conexión:

```bash
python3 /data/.openclaw/workspace/scripts/google_calendar_oauth.py test
```
