import requests

def get_ip_info():
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        response.raise_for_status()
        ip = response.json()["ip"]
        print(f"🌍 Your public IP address is: {ip}")
    except requests.RequestException as e:
        print(f"❌ Error fetching IP address: {e}")

if __name__ == "__main__":
    get_ip_info()
