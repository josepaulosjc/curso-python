lista = []

print(type(lista))
#print(dir(lista))
#print(help(list))

print(len(lista))
lista.append(1)
lista.append(5)
lista.append([1,2,3])

print(lista)
print(len(lista)) 

nova_lista = [1, 5, 'Ana', 'Bia']
print(nova_lista)

nova_lista.remove(5)
print(nova_lista)

nova_lista.reverse() # COmo a lista é um objeto mutável, o reverse reverte a lista e já atribui seus valores
print(nova_lista)