### ATENÇÃO ##
## DICIONÁRIOS NÃO SÃO OBJETOS EM PYTHON ##

variavel = 'sexo'
pessoa = { 'nome': 'Prof(a) Ana', 'idade': 38, 'cursos': ['Ingles','Portugues'], variavel:'Feminino'}
print(type(pessoa))
print(len(pessoa))
print(pessoa)
print(pessoa['nome'])           # Prof(a) Ana
print(pessoa['idade'])          # 38
print(pessoa['cursos'])         # ['Ingles', 'Portugues']
print(pessoa['cursos'][1])      # Portugues
print(pessoa.keys())            # dict_keys(['nome', 'idade', 'cursos', 'sexo'])
print(pessoa.values())          # dict_values(['Prof(a) Ana', 38, ['Ingles', 'Portugues'], 'Feminino'])
print(pessoa.items())           # dict_items([('nome', 'Prof(a) Ana'), ('idade', 38), ('cursos', ['Ingles', 'Portugues']), ('sexo', 'Feminino')])
print(pessoa.get('idade'))      # 38

# print(pessoa['tags'])         # Erro pois não existe
print(pessoa.get('tags'))       # Não dá erro
print(pessoa.get('tags',[]))    # '[]' valor vazio (default definido) em caso de não encontrar nada