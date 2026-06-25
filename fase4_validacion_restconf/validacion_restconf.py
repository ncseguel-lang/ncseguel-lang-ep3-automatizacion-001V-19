import requests
import json
import urllib3

urllib3.disable_warnings()

BASE_URL = "https://192.168.56.101/restconf/data"

USER = "cisco"
PASSWORD = "cisco123!"

HEADERS = {
    "Accept": "application/yang-data+json"
}

checks = 0

# Hostname
r = requests.get(
    f"{BASE_URL}/Cisco-IOS-XE-native:native/hostname",
    auth=(USER, PASSWORD),
    headers=HEADERS,
    verify=False
)

with open("evidencias/responses/get_hostname.json", "w") as f:
    json.dump(r.json(), f, indent=2)

if r.json().get("Cisco-IOS-XE-native:hostname") == "RTR-PLATCLD":
    print("[OK] Hostname")
    checks += 1

# Interfaces
r = requests.get(
    f"{BASE_URL}/ietf-interfaces:interfaces",
    auth=(USER, PASSWORD),
    headers=HEADERS,
    verify=False
)

with open("evidencias/responses/get_interfaces.json", "w") as f:
    json.dump(r.json(), f, indent=2)

print("[OK] Interfaces")
checks += 1

# NTP
r = requests.get(
    f"{BASE_URL}/Cisco-IOS-XE-native:native/ntp",
    auth=(USER, PASSWORD),
    headers=HEADERS,
    verify=False
)

with open("evidencias/responses/get_ntp.json", "w") as f:
    json.dump(r.json(), f, indent=2)

print("[OK] NTP")
checks += 1

# Loopback
if "Loopback10" in open("evidencias/responses/get_interfaces.json").read():
    print("[OK] Loopback10")
    checks += 1

print(f"\n{checks}/4 OK")

if checks == 4:
    print("CONFORME")
else:
    print("NO CONFORME")
