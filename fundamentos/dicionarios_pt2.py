pessoa = { 'nome': 'Prof Alberto', 'idade': 43, 'cursos': ['React','Python']}

pessoa['idade'] = 44
pessoa['cursos'].append('Angular')

print(pessoa)

pessoa.pop('idade')  # Executa, Lê e remove o valor
print(pessoa)
pessoa.update({'idade': 44, 'sexo': 'M'})
print(pessoa)

del pessoa['cursos']
print(pessoa)

pessoa.clear()
print(pessoa)