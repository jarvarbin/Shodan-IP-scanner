import shodan
from socket import *

# create a Shodan client
shodan_client = shodan.Shodan("YOUR_API_KEY")

# set the target IP and ports to scan
ip = "8.8.8.8"
ports = [21, 22, 23, 25, 53, 80, 110, 443]

# scan the target IP for open ports
for port in ports:
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((ip, port))
    if result == 0:
        print(f"Port {port} is open on {ip}")
        # check for vulnerabilities using the Shodan API
        try:
            host = shodan_client.host(ip)
            print(f"Vulnerabilities found on {ip}:")
            for vulnerability in host['vulns']:
                print(f"- {vulnerability}")
        except Exception as e:
            print(f"Error: {e}")
    s.close()
