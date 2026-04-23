#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 2 ]; then
  echo "Uso: $0 <slug> <tipo> [nombre_humano]"
  echo "Tipos: producto | cliente | infraestructura | laboratorio"
  exit 1
fi

ROOT="/data/.openclaw/workspace"
SLUG="$1"
TYPE="$2"
HUMAN_NAME="${3:-$1}"
PROJECT_DIR="$ROOT/projects/$SLUG"
TEMPLATE_DIR="$ROOT/projects/_template"

if [ -e "$PROJECT_DIR" ]; then
  echo "El proyecto ya existe: $PROJECT_DIR"
  exit 1
fi

mkdir -p "$PROJECT_DIR"/{docs,deliverables,scripts,skills,assets}

cat > "$PROJECT_DIR/README.md" <<README
# $HUMAN_NAME

## Identidad
- Nombre: $HUMAN_NAME
- Slug: $SLUG
- Tipo: $TYPE
- Estado: activo

## Objetivo
Describe en una frase qué resuelve este proyecto.

## Resultado esperado
Qué tendría que existir para considerarlo útil o terminado.

## Stack
- GitHub repo: pendiente
- Scripts específicos: \
  - 
- Skills específicas: \
  - 
- Integraciones: \
  - 

## Reglas operativas
- Qué sí toca aquí
- Qué no toca aquí
- Qué dependencias comparte con otros proyectos

## Próximos pasos
- 
README

echo "Proyecto creado en: $PROJECT_DIR"
echo "Siguiente paso recomendado: crear repo GitHub con nombre '$SLUG'"
