#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

echo "→ Levantando PostgreSQL..."
docker compose up -d db

echo "→ Esperando que la base esté lista..."
until docker compose exec -T db pg_isready -U "${POSTGRES_USER:-vacaciones}" -d "${POSTGRES_DB:-vacaciones}" >/dev/null 2>&1; do
  sleep 1
done

echo "→ Iniciando bot (escribí abajo cuando veas el menú)..."
echo ""
exec docker compose run --build --rm bot
