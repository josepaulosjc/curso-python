import requests


print("1) Tentando pegar o usuario 1 inexistente:")
url = 'http://localhost:8080/usuarios/1'
res = requests.get(url)
print(res.content)


#adicona o usuario 1
print("\n2) Adicionando o usuario 1:")
url = 'http://localhost:8080/usuarios'
dados = {"id": 1, "email":"fulano@teste.com"}
res2 = requests.post(url, json=dados)
print(res2.status_code, res2.headers)

#tenta pegar o usuario 1 novamente
print("\n3) Pegando novamente usuario 1:")
url = 'http://localhost:8080/usuarios/1'
res3 = requests.get(url)
print(res3.json())

#tenta adicionar novamente o usuario 1
print("\n4) Adicionando novamente o usuario 1:")
url = 'http://localhost:8080/usuarios'
dados = {"id": 1, "email":"fulano@teste.com"}
res4 = requests.post(url, json=dados)
print(res4.status_code, res4.json())

#altera email do usuario 1
print("\n5) Alterando o email do usuario 1:")
url = 'http://localhost:8080/usuarios/1'
dados = {"id": 1, "email":"fulano@novo.com"}
res5 = requests.put(url, json=dados)
print(res5.status_code)

# tenta alterar email do usuario 2
print("\n6) Tentando alterar o email do usuario 2 (inexistente):")
url = 'http://localhost:8080/usuarios/2'
dados = {"id": 1, "email":"fulano@novo.com"}
res6 = requests.put(url, json=dados)
print(res6.status_code, res6.json())

#apaga usuario 1
print("\n7) Apagando o usuario 1:")
url = 'http://localhost:8080/usuarios/1'
res7 = requests.delete(url)
print(res7.status_code)

#tenta pegar o usuario 1 novamente (inexistente)
print("\n8) Pegando novamente usuario 1 (inexistente):")
url = 'http://localhost:8080/usuarios/1'
res8 = requests.get(url)
print(res8.json())