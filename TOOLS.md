# TOOLS

## Qué es este archivo

`TOOLS.md` guarda notas locales y operativas del entorno.

Su función es reunir valores específicos de esta instalación que hacen falta para operar bien.

## Configuración y secretos

Incluye aquí solo dónde viven las cosas, no su contenido completo.

### Rutas de configuración

- **.env canónico:** no existe ahora mismo en esta instalación (`/data/.openclaw/.env` está ausente)
- **Config de plataforma:** `/data/.openclaw/openclaw.json`
- **Workspace principal:** `/data/.openclaw/workspace`
- **Skills locales:** `/data/.openclaw/skills`
- **Ruta de compatibilidad `/data/.clawbot/`:** no existe ahora mismo

### Regla de seguridad

- documenta ubicación y propósito
- evita pegar secretos enteros en el archivo
- si un valor es especialmente sensible, referencia su ubicación, no el contenido

## Mensajería

### Plataforma principal

- **Proveedor:** Telegram
- **Bot/cuenta:** TanqueBot (`@lacajaambarBot`)
- **Canal principal activo:** chat directo `1356520901`
- **Política actual:** DM por pairing y grupos por allowlist

### Topics, threads o subcanales

- No hay topics, threads ni subcanales activos en este chat directo.

### Comportamiento por topic

- No configurado todavía, porque el canal principal actual es un DM de Telegram.

### Plataforma secundaria

- No hay otra plataforma activa documentada en esta instalación.

## Gestión de proyectos

- **Workspace o espacio principal:** `/data/.openclaw/workspace`
- **Proyecto operativo principal:** Orquesta
- **Skill de personalidad reusable:** `/data/.openclaw/skills/tanque-persona`
- **Memoria diaria:** `/data/.openclaw/workspace/memory/`
- **Memoria curada:** `/data/.openclaw/workspace/MEMORY.md`

## CLIs y utilidades

- **CLI de email:** `/usr/local/bin/himalaya`
- **Config del CLI de email:** `~/.config/himalaya/config.toml`
- **CLI de agente o coding tool:** `/usr/local/bin/openclaw`
- **Python principal:** `/usr/bin/python3`
- **Node principal:** `/usr/local/bin/node`
- **Git principal:** `/usr/bin/git`
- **Logs:** `/data/.openclaw/logs`
- **Logs clave:** `/data/.openclaw/logs/config-audit.jsonl`, `/data/.openclaw/logs/config-health.json`
- **Base de datos o mirror local:** no hay una base local dedicada en `/data/.openclaw/state`; el estado útil visible está repartido entre `workspace/`, `logs/` y `openclaw.json`
- **Helper local de transcripción:** `/data/.openclaw/workspace/scripts/whisper-transcribe.py`
- **Artefactos temporales útiles:** `/data/.openclaw/workspace/tmp`

## Infraestructura local

### Hosts y aliases

- `openclaw-local` → instalación principal en `/data/.openclaw`
- `gateway-local` → gateway OpenClaw local en `http://127.0.0.1:18789`
- `workspace-main` → workspace operativo en `/data/.openclaw/workspace`

### Paths o endpoints útiles

- `http://127.0.0.1:18789` → gateway local
- `/data/.openclaw/logs/config-audit.jsonl` → log de auditoría de config
- `/data/.openclaw/logs/config-health.json` → estado/health de config

### Reglas operativas del entorno

- El TTS está configurado en `openclaw.json` con proveedor Microsoft, modo `inbound`, voz `es-ES-XimenaNeural`, velocidad `+12%` y pitch `-2Hz`.
- Para voz entrante, la transcripción fiable ahora mismo pasa por el helper local de Whisper.
- La configuración canónica de plataforma vive en `openclaw.json`, no en un `.env`.
- No asumir topics o threads en Telegram salvo que aparezcan en metadata o en un grupo con topics.
- Para mensajería externa sensible, confirmar antes de enviar emails o publicaciones.
- El gateway local esperado escucha en `127.0.0.1:18789`.

## Stack de prompts o runtime

- **Modelo principal:** `openai-codex/gpt-5.4`
- **Auth visible del modelo:** perfil OAuth `openai-codex:cruzciudadboiza77@gmail.com`
- **Thinking por defecto:** `low`
- **Web search:** Perplexity habilitado
