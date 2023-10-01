import requests
from time import sleep

for c in range(15):
    response = requests.get('https://www.cloudflare.com/rate-limit-test')
    print(response.status_code)
    sleep(6)
