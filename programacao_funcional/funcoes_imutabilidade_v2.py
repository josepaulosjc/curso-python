from functools import reduce
from operator import add

# Lista Mútavel
valores = (30, 10, 25, 70, 100, 94)
print(sorted(valores))  # Ordenam mas não altera a lista (Procedural)
print(valores)

# valores.sort()  # Ordena e altera a lista (Funcao Interna da lista)
# print(valores)

print(max(valores))
print(min(valores))
print(sum(valores))
print(reduce(add, valores))
print(list(reversed(valores)))

print(valores)
