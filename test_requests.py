import requests

site_trybe = requests.get('https://www.betrybe.com/')
# print(site_trybe.status_code)
# print(site_trybe.headers['content-type'])

# print(site_trybe.content.decode('utf-8'))
# print(site_trybe.text)

# print(site_trybe.content)

# ===================================================================================
# httpbin = requests.post('https://httpbin.org/post', data='some content')
# print(httpbin.text)

# ===================================================================================
# httpbin = requests.get('https://httpbin.org/get', headers={"Accept": "application/json"})
# print(httpbin.text)

# ===================================================================================
# image = requests.get('https://httpbin.org/image/png')
# print(image.content)

# ===================================================================================
# response = requests.get('https://httpbin.org/get')
# print(response.json())

# ===================================================================================
# error case
response = requests.get('https://httpbin.org/status/404')
response.raise_for_status()