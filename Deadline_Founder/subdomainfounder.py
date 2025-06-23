import requests
import socket
from datetime import datetime
import json

# Subdomain tarayıcı
def get_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print("❌ Error fetching subdomains.")
            return []

        data = response.json()
        subdomains = set()

        for entry in data:
            name = entry.get("name_value", "")
            for sub in name.split("\n"):
                if sub.endswith(domain):
                    subdomains.add(sub.strip())

        return sorted(subdomains)

    except requests.exceptions.RequestException:
        print("❌ Network error.")
        return []

# Basit port tarayıcı
def scan_ports(host, start=20, end=1024):
    open_ports = []
    for port in range(start, end + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                if s.connect_ex((host, port)) == 0:
                    open_ports.append(port)
        except Exception:
            pass
    return open_ports

# HTTP header checker
def get_headers(url):
    try:
        response = requests.get(f"http://{url}", timeout=5)
        return dict(response.headers)
    except Exception:
        return {}

# Main başlangıç
target = input("🔍 Enter root domain (example.com): ").strip()
subdomains = get_subdomains(target)

if not subdomains:
    print("No subdomains found.")
    exit()

with open("subdomains.txt", "w") as f:
    for sub in subdomains:
        f.write(sub + "\n")

print(f"\n✅ {len(subdomains)} subdomains saved to subdomains.txt\n")

for sub in subdomains:
    print(f"🔧 Processing {sub}...")

    # Port taraması
    try:
        ip = socket.gethostbyname(sub)
        ports = scan_ports(ip)
        with open(f"open_ports_{sub.replace('.', '_')}.txt", "w") as pf:
            for p in ports:
                pf.write(f"{p}\n")
        print(f"  ➤ Found {len(ports)} open ports.")

    except Exception:
        print(f"  ⚠️ Could not resolve {sub}")
        continue

    # Header taraması
    headers = get_headers(sub)
    with open(f"headers_{sub.replace('.', '_')}.txt", "w") as hf:
        for k, v in headers.items():
            hf.write(f"{k}: {v}\n")
        if not headers:
            hf.write("No headers or connection failed.\n")

    print(f"  ✅ Headers written.\n")

print("🎯 All tasks completed.")
