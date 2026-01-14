ZENDESK MACRO IMPORTER

Purpose
Import Zendesk macros from a CSV file using the Zendesk Macros API.

Files
data/fts_zendesk_macros_api_import.csv
scripts/import_macros.py
postman/collection.json
postman/env.example.json
postman/pre_request_script.js
run.sh

Python quick start
Set env vars:
ZENDESK_SUBDOMAIN=YOUR_SUBDOMAIN
ZENDESK_EMAIL=YOUR_ADMIN_EMAIL
ZENDESK_API_TOKEN=YOUR_API_TOKEN
CSV_PATH=data/fts_zendesk_macros_api_import.csv

Run:
./run.sh

Postman quick start
Import:
postman/collection.json
postman/env.example.json

Fill environment values:
subdomain
email
api_token

Runner:
Request: Create Macro From CSV Row
Data file: data/fts_zendesk_macros_api_import.csv
Delay: 200 ms

Auth test
Run: Auth Test - Users Me
Expected: HTTP 200
