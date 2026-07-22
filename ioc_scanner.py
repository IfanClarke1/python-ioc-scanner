from datetime import datetime

# Starts the output with "IOC Scan Started"
print ("IOC Scan Started", datetime.now())

# Takes the IP addresses from the Log file and the Malicious IP file
log_ips = open("log_ips.txt").read().splitlines()
malicious_ips = open("malicious_ips.txt").read().splitlines()

# Starts the alert counter
alerts = 0

# Compares the log IPs against the malicious IPs
for ip in log_ips:
  if ip in malicious_ips:
    alerts += 1
    # Increments the counter and flags a high-severity alert
    print(f"[HIGH] Malicious IP detected: {ip}")

# Prints the final number of alerts
print(f"\nTotal alerts: {alerts}")
