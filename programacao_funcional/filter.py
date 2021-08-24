pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17},
]

menores = list(filter(lambda p: p['idade'] < 18, pessoas))
nomes_grandes = list(filter(lambda p: len(p['nome']) > 6, pessoas))
print(menores)
print(nomes_grandes)
