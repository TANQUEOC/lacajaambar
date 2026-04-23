# TECH PROJECTS

Esta es la organización oficial de proyectos TECH dentro del workspace.

## Regla base

Cada proyecto vive aislado dentro de `projects/<slug>/`.

Objetivo:
- separar contexto
- separar documentación
- permitir skills específicas por proyecto
- permitir repositorios GitHub distintos
- evitar mezclar cambios entre clientes, productos y experimentos

## Estructura

```text
projects/
  _template/
  tanque-general/
  orquesta/
  cliente-ceramica/
  taller-vehiculos/
  labs/
  shared-infra/
```

## Convención por proyecto

Cada proyecto debe tender a tener esta forma:

```text
projects/<slug>/
  README.md
  docs/
  deliverables/
  scripts/
  skills/
  assets/
```

### Significado

- `README.md`: identidad del proyecto, objetivo, estado, stack y reglas.
- `docs/`: documentación de producto, arquitectura, decisiones y notas de trabajo.
- `deliverables/`: entregables listos para cliente, propuesta o publicación.
- `scripts/`: automatizaciones y utilidades específicas de ese proyecto.
- `skills/`: skills o subskills pensadas para ese proyecto concreto.
- `assets/`: recursos visuales, textos base, referencias y material reutilizable.

## Cómo se decide a qué proyecto aplicar cambios

Regla operativa:
- si Luis nombra un proyecto explícitamente, se trabaja ahí
- si el hilo actual ya venía sobre un proyecto, se mantiene ese contexto hasta que cambie
- si hay ambigüedad, se pregunta o se propone la mejor coincidencia

## Regla de GitHub

Cada proyecto TECH puede tener su propio repositorio.

Ejemplo recomendado:
- `projects/tanque-general` → repo GitHub propio
- `projects/orquesta` → repo GitHub propio cuando madure
- `projects/cliente-ceramica` → repo separado si el cliente lo requiere
- `projects/taller-vehiculos` → repo separado si el cliente lo requiere

## Regla de skills

Las skills reutilizables globales viven fuera, en el ecosistema general.
Las skills muy específicas deben vivir dentro del proyecto correspondiente, en `projects/<slug>/skills/`.

## Proyectos actuales

- `tanque-general`: repo general de software y base técnica conectada a GitHub.
- `orquesta`: núcleo conceptual y operativo del sistema Orquesta.
- `cliente-ceramica`: vertical comercial/digital para empresa cerámica.
- `taller-vehiculos`: vertical de voz, agenda y atención para taller.
- `labs`: pruebas, ideas y prototipos que todavía no merecen proyecto formal.
- `shared-infra`: piezas comunes reutilizables entre proyectos.
