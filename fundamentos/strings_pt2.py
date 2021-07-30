nome = 'Ana Paula'
print(nome[0])  # 'A'
print(nome[6])  # 'U'
print(nome[-3])  # Ainda 'U' da direita para esqueda
print(nome[4:])  # 'Paula' 4 en diante
print(nome[-5:]) # 'Paula' também da direita para esquerda

print(nome[:3]) # 'Ana' parte do indice 0 até 2 e para no 3
print(nome[:5]) # 'Ana P' parte do indice 0 até 4 e para no 5
print(nome[1:5]) # 'na P' parte do indice 1 até 4 e para no 5
print(nome[::]) # 'Ana Paula' string completa

numeros = '1234567890'
print(numeros[0])   # 1
print(numeros[::])  # todos
print(numeros[::2]) # 13579  - O ultimo valor é o step e vai de 2 em 2 
print(numeros[1::2]) # 2468  - O ultimo valor é o step e vai de 2 em 2 

print(numeros[::-1]) # Invertendo string
print(numeros[::-2]) # Invertendo string de dois em dois

print(nome[::-1]) # Invertendo nome
