'''
CONJUNTOS:
1) Não aceitam repetição de valores, (são ignoradas)
2) Não é uma estrutura indexada
3) Não garante ordenação
'''

a = {1, 2, 3}
print(type(a))

a = set('coddd3r')
print(a)
print( '3' in a, 4 not in a )

# comparação
print({1, 2, 3} == {3, 2, 1, 3})

c1 = {1, 2}
c2 = {2, 3}

print(c1.union(c2))         # Union
print(c1.intersection(c2))  # Interssection
c1.update(c2)               # Union
print(c1)

print(c2 <= c1)             # C2 é subconjunto de c1 ?
print(c1 >= c2)

print({1, 2, 3} - {2})      # Subtração de conjunto
print( c1 - c2 )

c1 -= {3}                   # Subtraindo e atibuindo ao c1
print(c1)