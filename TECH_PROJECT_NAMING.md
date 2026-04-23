# TECH PROJECT NAMING

## Regla general

Usa nombres cortos, claros y estables.

Cada proyecto TECH debe tener:
- **nombre humano**: legible para conversación
- **slug local**: nombre de carpeta
- **repo GitHub**: nombre del repositorio
- **skill namespace**: prefijo de skills del proyecto

## Convención recomendada

### 1. Nombre humano
Formato natural, fácil de leer.

Ejemplos:
- TanqueGeneral
- Orquesta
- Cliente Cerámica
- Taller Vehículos

### 2. Slug local
Formato:
- minúsculas
- palabras separadas por guion medio
- sin espacios
- sin tildes
- sin caracteres raros

Ejemplos:
- `tanque-general`
- `orquesta`
- `cliente-ceramica`
- `taller-vehiculos`
- `shared-infra`

### 3. Repo GitHub
Usar el mismo slug que el proyecto local salvo que haya una razón fuerte para no hacerlo.

Ejemplos recomendados:
- `tanque-general`
- `orquesta`
- `cliente-ceramica`
- `taller-vehiculos`

### 4. Skills del proyecto
Guardar las skills dentro de:
- `projects/<slug>/skills/`

Convención recomendada para nombrarlas:
- `<slug>-<skill>`

Ejemplos:
- `orquesta-playbooks`
- `cliente-ceramica-catalogo`
- `taller-vehiculos-citas`

## Tipos de proyecto

### Producto
Slug corto y directo.
Ejemplo:
- `orquesta`

### Cliente
Prefijo por cliente o vertical.
Ejemplo:
- `cliente-ceramica`
- `taller-vehiculos`

### Infraestructura compartida
Usar nombres funcionales.
Ejemplo:
- `shared-infra`
- `voice-stack`
- `calendar-core`

### Laboratorio
Si algo es temporal, empieza en `labs/` antes de crear repo.

## Regla de decisión

Si un nombre necesita demasiada explicación, probablemente está mal.

Prioriza:
- claridad
- estabilidad
- reusabilidad
- facilidad para decirlo en chat
