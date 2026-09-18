import subprocess
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
    "FastenHealth/fasten-onprem",
    "AWELL-HEALTH/orchestration-stories",
    "kresusapp/kresus",
    "danny-avila/LibreChat",
    "elixir-circuits/circuits_gpio"
]

results = {}

for r in set(repos):
    cmd = ["gh", "api", f"repos/{r}", "--jq", ".stargazers_count"]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        results[r] = int(res.stdout.strip())
    except Exception as e:
        print(f"Error fetching {r}: {e}")
        results[r] = 0

with open(r"C:\Users\hp\Documents\Projects\Awesome-Medication-Adherence-Platform\stars.json", "w") as f:
    json.dump(results, f, indent=2)

print("Fetched stars for", len(results), "repos")
