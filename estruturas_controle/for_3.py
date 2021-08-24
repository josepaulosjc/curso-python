produto = {'nome': 'Caneta Chiic', 'preco': 14.99,
           'importada': True, 'estoque': 793}

for chave in produto:
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(f'{chave} = {valor}')

print('Variavel disponivel mesmo depois do bloco')
print(f'{chave} = {valor}')
