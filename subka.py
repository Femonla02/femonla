import requests

def check_subdomain(domain, subdomain):
    url = f"http://{subdomain}.{domain}"
    try:
        response = requests.head(url)
        if response.status_code == 200:
            print(f"Found: {url}")
    except requests.ConnectionError:
        pass

def main():
    domain = input("Enter the domain to scan (e.g., example.com): ")
    subdomains = [
        "www", "mail", "ftp", "webmail", "blog", "api", "test", "dev", "m", "secure"
        # Add more subdomains as needed
    ]

    for subdomain in subdomains:
        check_subdomain(domain, subdomain)

if __name__ == "__main__":
    main()
