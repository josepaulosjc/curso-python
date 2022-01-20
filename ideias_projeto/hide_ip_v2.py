import json
import requests
import proxyscrape

#https://www.freeproxylists.net/
# proxies = {
#     'https': 'https://112.78.170.251:8080',
#     'http': 'http://112.78.170.251:8080'
# }

# url = 'http://httpbin.org/ip'
# req = requests.get(url, proxies=proxies)
# print(req.json()["origin"])

collector = proxyscrape.create_collector('my-collector', 'http')  # Create a collector for http resources
proxy = collector.get_proxies()
proxy = f"https://{proxy[0].host}:{proxy[0].port}"
print(proxy)

proxies = {
    'http': proxy
}

url = 'http://httpbin.org/ip'
req = requests.get(url, proxies=proxies)
print(req.json()["origin"])

