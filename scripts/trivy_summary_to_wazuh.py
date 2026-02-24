import json
import sys
import datetime
import subprocess

def count_vulnerabilities(report):
    counts = {
        "CRITICAL": 0,
        "HIGH": 0,
        "MEDIUM": 0,
        "LOW": 0
    }

    for result in report.get("Results", []):
        for vuln in result.get("Vulnerabilities", []) or []:
            severity = vuln.get("Severity")
            if severity in counts:
                counts[severity] += 1

    return counts

if __name__ == "__main__":
    report_file = sys.argv[1]
    image_name = sys.argv[2]

    try:
        with open(report_file) as f:
            report = json.load(f)
    except:
        report = {}

    counts = count_vulnerabilities(report)
    total = sum(counts.values())

    commit = subprocess.getoutput("git rev-parse --short HEAD")

    event = {
        "event_type": "devsecops_trivy_scan",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "repository": "devsecops-sonar",
        "branch": "main",
        "commit": commit,
        "image": image_name,
        "critical_count": counts["CRITICAL"],
        "high_count": counts["HIGH"],
        "medium_count": counts["MEDIUM"],
        "low_count": counts["LOW"],
        "total_vulnerabilities": total,
        "status": "FAILED" if counts["CRITICAL"] > 0 else "PASSED"
    }

    print(json.dumps(event))
