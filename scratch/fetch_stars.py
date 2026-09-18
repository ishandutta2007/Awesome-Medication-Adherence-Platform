import urllib.request
import json
import time

repos = [
    "DanielVolz/medassist-ng",
    "njic/medassist",
    "damacus/med-tracker",
    "Futsch1/medTimer",
    "AdamGuidarini/MediTrak",
    "Qitalach/PillApp",
    "cucumberfalse/takeyourmeds",
    "manuel-array/pilldor",
    "MBombeck/HealthLog",
    "openemr/openemr",
    "gnuhealth/gnuhealth",
    "openmrs/openmrs-core",
    "Bahmni/bahmni",
    "hapifhir/hapi-fhir",
    "FirelyTeam/firely-net-sdk",
    "medplum/medplum",
    "google/open-health-stack",
    "binwiederhier/ntfy",
    "gotify/server",
    "novuhq/novu",
    "caronc/apprise",
    "calcom/cal.com",
    "nextcloud/calendar",
    "nextcloud/server",
    "metabase/metabase",
    "apache/superset",
    "grafana/grafana",
    "keycloak/keycloak",
    "openfga/openfga",
    "openbao/openbao",
    "eclipse-mosquitto/mosquitto",
    "node-red/node-red",
    "thingsboard/thingsboard",
    "home-assistant/core",
    # Add new open-source repos to fetch stars for:
    "FastenHealth/fasten-onprem",
    "AWELL-HEALTH/orchestration-stories",
    "kresusapp/kresus",
    "danny-avila/LibreChat",
    "elixir-circuits/circuits_gpio"
]

results = {}
headers = {'User-Agent': 'Mozilla/5.0'}

for r in set(repos):
    url = f"https://api.github.com/repos/{r}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            results[r] = data.get("stargazers_count", 0)
    except Exception as e:
        print(f"Error fetching {r}: {e}")
        results[r] = 0
    time.sleep(0.1)

with open("scratch/stars.json", "w") as f:
    json.dump(results, f, indent=2)

print("Fetched stars for", len(results), "repos")
