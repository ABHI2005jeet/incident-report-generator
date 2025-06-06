import re
import csv

# File paths
log_file = "sample.log"
report_file = "incident_report.csv"

# Pattern to match log entries
log_pattern = re.compile(r'^(?P<timestamp>[\d\-T:+\.]+)\s+(?P<host>\S+)\s+(?P<source>[^\[]+)(?:\[(?P<pid>\d+)\])?:\s+(?P<message>.+)$')

# List to hold parsed data
parsed_logs = []

# Read and parse log lines
with open(log_file, "r") as file:
    for line in file:
        match = log_pattern.match(line)
        if match:
            log_data = match.groupdict()

            # Filter condition (only keep lines with "login" or "error")
            if "login" in log_data["source"] or "error" in log_data["message"].lower():
                parsed_logs.append(log_data)

        if match:
            parsed_logs.append(match.groupdict())

# Write to CSV
with open(report_file, "w", newline="") as csvfile:
    fieldnames = ["timestamp", "host", "source", "pid", "message"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for log in parsed_logs:
        writer.writerow(log)

print(f"[+] Report generated: {report_file}")
 
