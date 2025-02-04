import requests
import argparse

def lookup_ip(ip):
    try:
        url = f"https://ipinfo.io/{ip}/json"
        response = requests.get(url, timeout=5)
        if response.status_code == 404:
            print(f"Error: invalid IP address {ip}")
            return
        elif response.status_code == 200:
            data = response.json()
            print(f"IP info for {ip}:")
            print("===============================")
            print(f"City: {data.get('city', '')}")
            print(f"Region: {data.get('region', '')}")
            print(f"Country: {data.get('country', '')}")
            print(f"Location: {data.get('loc', '')}")
            print(f"ISP: {data.get('org', '')}")
            print(f"Postal Code: {data.get('postal', '')}")
            print("===============================\n")
    except (requests.RequestException, ValueError) as e:
        print(f"An unexpected error occured while looking up {ip}:", type(e).__name__)

def lookup_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            ips = [line.strip() for line in file if line.strip()]
            for ip in ips:
                lookup_ip(ip)
    except FileNotFoundError:
        print(f"Error: file '{file_path}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {type(e).__name__}")

def main():
    parser = argparse.ArgumentParser(description="IP Information Lookup Tool")
    parser.add_argument("ip", nargs="?", help="Single IP address to look up")
    parser.add_argument("-f", "--file", help="Path to a file containing a newline-separated list of IP addresses")
    args = parser.parse_args()

    if args.file:
        lookup_from_file(args.file)
    elif args.ip:
        lookup_ip(args.ip)
    else:
        print("Usage: python ipinfo_lookup.py <IP address> OR python ipinfo_lookup.py -f <file>")


if __name__ == "__main__":
    main()