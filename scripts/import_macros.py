#!/usr/bin/env python3
import base64, csv, json, os, sys, time, urllib.request, urllib.error

def require_env(name: str) -> str:
    v = os.getenv(name, "").strip()
    if not v:
        raise SystemExit(f"Missing required env var: {name}")
    return v

def request(method: str, url: str, auth_header: str, payload=None):
    req = urllib.request.Request(url, method=method)
    req.add_header("Authorization", auth_header)
    req.add_header("Content-Type", "application/json")
    data = None
    if payload is not None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    try:
        with urllib.request.urlopen(req, data=data) as resp:
            return resp.status, resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8")

def main():
    subdomain = require_env("ZENDESK_SUBDOMAIN")
    email = require_env("ZENDESK_EMAIL")
    token = require_env("ZENDESK_API_TOKEN")
    csv_path = require_env("CSV_PATH")

    creds = f"{email}/token:{token}"
    b64 = base64.b64encode(creds.encode("utf-8")).decode("utf-8")
    auth = f"Basic {b64}"

    url = f"https://{subdomain}.zendesk.com/api/v2/macros.json"

    created = failed = 0
    with open(csv_path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for i, row in enumerate(reader, start=1):
            title = (row.get("title") or "").strip()
            active_raw = (row.get("active") or "true").strip().lower()
            active = active_raw in ("true","1","yes","y")
            try:
                actions = json.loads(row.get("actions_json") or "[]")
            except json.JSONDecodeError as e:
                failed += 1
                print(f"[{i}] failed: {title} | invalid actions_json | {e}")
                continue

            payload = {"macro": {"title": title, "active": active, "actions": actions}}
            status, body = request("POST", url, auth, payload)

            if 200 <= status < 300:
                created += 1
                print(f"[{i}] created: {title}")
            else:
                failed += 1
                print(f"[{i}] failed: {title} | HTTP {status} | {body}")
            time.sleep(0.2)

    print(f"Done. Created={created} Failed={failed}")
    if failed:
        sys.exit(1)

if __name__ == "__main__":
    main()
