from functools import reduce

pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17},
]

soma_idades = reduce(lambda idades, p: idades + p['idade'], pessoas, 0)
print(soma_idades)

# Podemos utilizar os conceitos juntos

# Fazendo Map, Filter e Reduce
apenas_idades = list(map(lambda p: p['idade'], pessoas))    # MAP
menores = list(filter(lambda idade: idade < 18, apenas_idades))  # FILTER
soma_menores = reduce(lambda idades, idade: idade +
                      idade, menores, 0)  # REDUCE
print(soma_menores)
