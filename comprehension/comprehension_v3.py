#!python
# [ expressão for item in list if condicional ]
# USANDO GENERATOR ele utilizará menos memória do que o List Comprehension

generator = (i ** 2 for i in range(10) if i % 2 == 0)
print(next(generator))  # Saída 0
print(next(generator))  # Saída 4
print(next(generator))  # Saída 16
print(next(generator))  # Saída 36
print(next(generator))  # Saída 64
# print(next(generator)) # Erro!


# Forma Normal
dobros = []
for i in range(10):
    if i % 2 == 0:
        dobros.append(i*2)
print(dobros)
