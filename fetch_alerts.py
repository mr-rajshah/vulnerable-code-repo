import requests

GITHUB_REPO = "mr-rajshah/vulnerable-code-repo"
GITHUB_TOKEN = "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"
import requests
import json

# Replace with your repository details
GITHUB_OWNER = "mr-rajshah"
REPO_NAME = "vulnerable-code-repo"
GITHUB_TOKEN = "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"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Fetch Code Scanning Alerts
def get_code_scanning_alerts():
    url = f"https://api.github.com/repos/{GITHUB_OWNER}/{REPO_NAME}/code-scanning/alerts"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch alerts:", response.json())
        return []

# Fetch Likelihood of Exploitability from CWE
def get_cwe_exploitability(cwe_id):
    url = f"https://cwe.mitre.org/data/definitions/{cwe_id}.html"
    response = requests.get(url)
    if "Likelihood of Exploitability: High" in response.text:
        return "High"
    return "Low/Medium"

# Main Execution
alerts = get_code_scanning_alerts()

print("Vulnerabilities with High Severity & High Exploitability:")
for alert in alerts:
    severity = alert.get("rule", {}).get("security_severity_level", "UNKNOWN")
    cwe_id = alert.get("rule", {}).get("cwe_ids", [None])[0]

    if severity in ["high", "critical"] and cwe_id:
        likelihood = get_cwe_exploitability(cwe_id)
        if likelihood == "High":
            print(f"Vulnerability: {alert['rule']['description']}")
            print(f"Severity: {severity}, CWE: {cwe_id}, Exploitability: {likelihood}")
            print("-" * 50)

