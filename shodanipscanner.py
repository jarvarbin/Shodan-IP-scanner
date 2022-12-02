import shodan
from socket import *
shodan_client = shodan.Shodan("YOUR_API_KEY")
ip = "8.8.8.8"
ports = [21, 22, 23, 25, 53, 80, 110, 443]
for port in ports:
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((ip, port))
    if result == 0:
        print(f"Port {port} is open on {ip}")
        try:
            host = shodan_client.host(ip)
            print(f"Vulnerabilities found on {ip}:")
            for vulnerability in host['vulns']:
                print(f"- {vulnerability}")
        except Exception as e:
            print(f"Error: {e}")
    s.close()
