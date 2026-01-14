#!/usr/bin/env bash
set -euo pipefail
: "${ZENDESK_SUBDOMAIN:?Missing ZENDESK_SUBDOMAIN}"
: "${ZENDESK_EMAIL:?Missing ZENDESK_EMAIL}"
: "${ZENDESK_API_TOKEN:?Missing ZENDESK_API_TOKEN}"
export CSV_PATH="${CSV_PATH:-data/fts_zendesk_macros_api_import.csv}"
python3 scripts/import_macros.py
