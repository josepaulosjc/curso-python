lista1 = [1, 2, 3]
dobro = map(lambda x: x * 2, lista1)
print(list(dobro))

lista2 = [
    {'nome': 'Joao', 'idade': 31},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'Jose', 'idade': 26},
]

apenas_nomes = list(map(lambda p: p['nome'], lista2))
print(apenas_nomes)

apenas_idades = list(map(lambda p: p['idade'], lista2))
print(apenas_idades)

soma_idades = sum(apenas_idades)
print(soma_idades)

# Desafio, retornar '<Nome> tem <idade> anos.'
frases = list(map(lambda p: f'{p["nome"]} tem {p["idade"]} anos.', lista2))
print(frases)
