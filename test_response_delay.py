import requests

# respose = requests.get('https://httpbin.org/delay/10')
# print(respose.status_code)


not_return = True

while not_return:
    try:
        print('try')
        respose = requests.get('https://httpbin.org/delay/10', timeout=2)
        print(respose)
    except requests.ReadTimeout:
        print('except')
        respose = requests.get('https://httpbin.org/delay/1', timeout=2)
        print(respose)
    finally:
        print(respose.status_code)
        not_return = False
