lista = ['Ana', 'Bia', 'Paula', 'Jonas', 'Pedro']
print(lista[1:3])       # 'Bia', 'Paula'
print(lista[1:-1])      # 'Bia', 'Paula', 'Jonas'
print(lista[:-1])       # 'Ana', 'Bia', 'Paula', 'Jonas'
print(lista[:])         # Toda Lista
print(lista[::2])       # 'Ana', 'Paula', 'Pedro'
print(lista[::-1])      # Reverse

del lista[2]            # 'Ana', 'Bia', 'Jonas', 'Pedro'
print(lista)

del lista[1:]            # 'Ana'
print(lista)