palavra = 'paralelepipedo'

for letra in palavra:
    print(letra, end=',')
print('Fim')

aprovados = ['Jose', 'Joyce', 'Hygor', 'Joao']

for nome in aprovados:
    print(nome)

# Trazendo o indice da Lista
for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)

dias_semana = ('Domingo', 'Segunda', 'Terça',
               'Quarta', 'Quinta', 'Sexta', 'Sábado')

for dia in dias_semana:
    print('Hoje e dia {}'.format(dia))

for numero in {1, 2, 3, 4, 5, 6}:
    print(numero)
