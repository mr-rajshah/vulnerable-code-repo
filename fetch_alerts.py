import requests

GITHUB_REPO = "mr-rajshah/vulnerable-code-repo"
GITHUB_TOKEN = "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"

HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"token {GITHUB_TOKEN}"
}

def get_code_scanning_alerts():
    url = f"https://api.github.com/repos/{GITHUB_REPO}/code-scanning/alerts"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        alerts = response.json()
        high_risk_alerts = []

        for alert in alerts:
            if alert.get("rule") and alert["rule"].get("severity") in ["high", "critical"]:
                cwe_id = alert["rule"].get("id", "Unknown")
                likelihood = get_cwe_likelihood(cwe_id)

                if likelihood == "High":
                    high_risk_alerts.append({
                        "CWE_ID": cwe_id,
                        "Severity": alert["rule"]["severity"],
                        "Likelihood of Exploitability": likelihood
                    })

        return high_risk_alerts
    else:
        print(f"Failed to fetch alerts: {response.status_code}")
        return []

def get_cwe_likelihood(cwe_id):
    """ Fetch likelihood from CWE database """
    cwe_likelihood_mapping = {
        "CWE-78": "High",   # Command Injection
        "CWE-79": "High",   # XSS
        "CWE-89": "High",   # SQL Injection
        "CWE-287": "Medium" # Improper Authentication
    }

    return cwe_likelihood_mapping.get(cwe_id, "Unknown")

if __name__ == "__main__":
    results = get_code_scanning_alerts()
    if results:
        print("High-risk vulnerabilities found:")
        for item in results:
            print(item)
    else:
        print("No high-risk vulnerabilities found.")
