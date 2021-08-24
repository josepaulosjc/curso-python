from string import Template

nome, idade = 'Ana', 30

# Interpolação com Tipagem ---- VERSÃO MAIS ANTIGA
print('Nome: %s  Idade: %d' % (nome, idade))

# Interpolação com indíce ---- VERSÂO RECOMENDADA para Python menor que 3.6 
print( 'Nome: {0}, Idade: {1}'.format(nome, idade))
print( 'Nome: {0}, Idade: {1}'.format(nome, idade))

# Iterpolção F String ----- VERSÃO NOVA MAIS RECOMENDADA a partir da versão 3.6
print( f'Nome: {nome}, Idade: {idade}' ) # Acrescentar 'f' de formatação

# Interpola e interpreta os valores em pythonn
print(f'{2 ** 8 + 1}') 

# Interpolação com Template
s = Template( 'Nome: $nome, Idade: $idade')
print(s.substitute(nome=nome, idade=idade))

