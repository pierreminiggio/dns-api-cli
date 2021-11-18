from config import *
import json
import requests
import sys

args = sys.argv

if len(args) != 2:
    print('Use like this : python main.py <sub_domain_name>')
    sys.exit()

sub_domain_name = args[1]
ip_request = requests.get('https://api.ipify.org')
current_ip = ip_request.text

dns_api_request = requests.put(
    dns_api_url,
    data=json.dumps({
        'domain': sub_domain_name,
        'ip': current_ip
    }),
    headers={
        'Authorization': 'Bearer ' + dns_api_token
    }
)

print(dns_api_request.status_code)
