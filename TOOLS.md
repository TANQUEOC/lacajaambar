# TOOLS

## Qué es este archivo

`TOOLS.md` guarda notas locales y operativas del entorno.

No define la filosofía del asistente.

No sustituye a las skills.

No es memoria curada del usuario.

Su función es muy concreta: reunir **valores específicos del entorno** que hacen falta para operar bien.

## Qué sí va aquí

- rutas locales
- IDs de canales, grupos, topics o threads
- nombres de hosts, aliases y endpoints
- ubicaciones de logs
- nombres de dispositivos
- preferencias técnicas del entorno
- ubicación de configs y secretos
- reglas prácticas que dependen de la instalación real

## Qué no va aquí

- principios de personalidad
- reglas generales de ejecución
- historia del proyecto
- preferencias humanas que pertenecen a `USER.md` o `MEMORY.md`
- documentación de skills compartidas

## Configuración y secretos

Incluye aquí solo dónde viven las cosas, no su contenido completo.

### Rutas de configuración

- **.env canónico:** /data/.openclaw/.env
- **Config de plataforma:** /data/.openclaw/openclaw.json
- **Symlinks o rutas de compatibilidad:** /data/.clawbot/

### Regla de seguridad

- documenta ubicación y propósito
- evita pegar secretos enteros en el archivo
- si un valor es especialmente sensible, referencia su ubicación, no el contenido

## Mensajería

### Plataforma principal

- **Canal o grupo principal:** chat id 1356520901 y la cuenta asociada es TanqueBot(@lacajaambarBot)

### Topics, threads o subcanales

-

### Comportamiento por topic

-

### Plataforma secundaria

-

### Proyectos y herramientas externas

-

## Gestión de proyectos

- **Workspace o espacio principal:**
- **Proyecto 1:**
- **Proyecto 2:**

## CLIs y utilidades

- **CLI de email:**
- **CLI de agente o coding tool:**
- **Logs:**
- **Base de datos o mirror local:**

## Infraestructura local

### Hosts y aliases

-

### Paths o endpoints útiles

-

### Reglas operativas del entorno

Guarda aquí reglas que dependen de cómo está montado el entorno real.

Ejemplos válidos:

- qué formato funciona mejor para notas de voz
- qué navegador o cuenta usar para cierto flujo
- qué endpoint es el bueno de un conector
- qué alias SSH está verificado
- qué validación visual hay que hacer antes de enviar algo

## Ejemplos de estructura

- **Notas de voz:**
- **Navegador o sesión recomendada:**
- **Regla de validación antes de enviar:**
- **Endpoint o conector activo:**

## Preferencias de contenido técnicas

Si hay preferencias del entorno que afectan a output o delivery técnico, pueden ir aquí.

Ejemplos:

- formato de audio preferido
- herramienta de conversión recomendada
- comportamiento de portapapeles o scripts helper
- stack de prompts activo y fallback

## Stack de prompts o runtime

- **Stack por defecto:**
- **Stack alternativo o fallback:**
- **Cómo se conmuta:**

## Mantenimiento

Un buen `TOOLS.md` debe ser:

- corto
- preciso
- local al entorno
- fácil de escanear
- fácil de actualizar

Si una nota deja de ser específica del entorno, probablemente debe mudarse a otro archivo.

## Principio final

`TOOLS.md` es la chuleta local del asistente.

No debería explicar el mundo.

Solo debería evitar que el asistente pierda tiempo buscando cosas que ya debería tener a mano.
