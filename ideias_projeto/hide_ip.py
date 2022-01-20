import json
import requests

url = 'http://httpbin.org/ip'

req = requests.get(url)

print(req.json()["origin"])