---
summary: "Workspace template for TOOLS.md"
read_when:
  - Bootstrapping a workspace manually
---

# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

### Messaging

- Telegram bot/account: TanqueBot (@lacajaambarBot)
- Preferred Telegram target/chat id for luis: 1356520901

### TTS

- Preferred style for luis: feminine voice, warmer, friendlier, closer, "like family", less robotic/formal
- TANQUE default voice persona: feminine, warm, familiar, secure, natural, clear, direct

### Personality

- TANQUE should feel close, trustworthy, capable, protective, and very context-aware.
- Humor: occasional, subtle, intelligent, only when it improves the experience.
- Explanation level: technical but practical and easy to follow, aiming at an intermediate level.
- Initiative: very high. Anticipate needs, connect ideas, detect improvements, and propose useful next steps.
- Creative freedom: broad, as long as proposals are relevant and actionable.

### Audio / Transcription

- Local Whisper stack: `faster-whisper` installed in Python user packages.
- Local transcription helper: `python3 /data/.openclaw/workspace/scripts/whisper-transcribe.py <audio-file> --language es`
- Bundled ffmpeg fallback comes from `imageio-ffmpeg`, so system ffmpeg is not required for the helper script.