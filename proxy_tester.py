import requests
import concurrent.futures

# .txt file of proxies that you want to test
with open('txt/random_proxy.txt') as f:
    proxylist = f.read().splitlines()

proxy_test = '87.103.175.250:9812'

good_proxies = []

def extract(proxy):
    try:
        response = requests.get('https://httpbin.org/ip', proxies = {'http': proxy, 'https': proxy}, timeout = 3)
        print(response.json(), ' - working')
        good_proxies.append(proxy)
    except:
        pass
    return proxy

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(extract, proxylist)

def write_proxies_to_file():
    goodproxylist = open('good_proxy.txt', 'w')
    for i in good_proxies:
        goodproxylist.write(f'{i}\n')
    goodproxylist.close()
    
print(good_proxies)
