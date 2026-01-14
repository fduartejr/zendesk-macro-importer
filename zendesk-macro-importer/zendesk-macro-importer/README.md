ZENDESK MACRO IMPORTER

Purpose
Import Zendesk macros from a CSV file using the Zendesk Macros API.

Quick start (Python)
1) Export env vars
ZENDESK_SUBDOMAIN=YOUR_SUBDOMAIN
ZENDESK_EMAIL=YOUR_ADMIN_EMAIL
ZENDESK_API_TOKEN=YOUR_API_TOKEN
CSV_PATH=data/fts_zendesk_macros_api_import.csv

2) Run
./run.sh

Postman
Import postman/collection.json
Import postman/env.example.json
Fill subdomain, email, api_token
Run Runner with data file: data/fts_zendesk_macros_api_import.csv
