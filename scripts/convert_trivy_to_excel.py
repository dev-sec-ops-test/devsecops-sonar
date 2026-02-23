import json
import pandas as pd
import sys

def convert(json_file, excel_file):
    try:
        with open(json_file) as f:
            data = json.load(f)
    except Exception:
        data = {}

    rows = []
    for result in data.get("Results", []):
        for vuln in result.get("Vulnerabilities", []) or []:
            rows.append({
                "Target": result.get("Target"),
                "VulnerabilityID": vuln.get("VulnerabilityID"),
                "PkgName": vuln.get("PkgName"),
                "InstalledVersion": vuln.get("InstalledVersion"),
                "Severity": vuln.get("Severity"),
                "Title": vuln.get("Title"),
            })

    df = pd.DataFrame(rows)
    df.to_excel(excel_file, index=False)

if __name__ == "__main__":
    convert(sys.argv[1], sys.argv[2])
