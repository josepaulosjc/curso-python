import requests
url = 'http://localhost:8080/api/add_message/1234'
dados = {"mytext":"lalala"}
res = requests.post(url, json=dados)
print(res.json())