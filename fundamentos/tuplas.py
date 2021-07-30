# As Tuplas não são mutáveis, não é possível alterar elementos

tupla = tuple()     # 1a Forma de fazer
tupla = ()          # 2a Forma de fazer

print(type(tupla))
#print(dir(tupla))
#print(help(tupla))

tupla = ('um')
print(type(tupla))

tupla = ('um' ,)
print(type(tupla))
print(tupla[0])
# tupla[0] = 'novo'   -> Não é possivel fazer atribuicao

cores = ('verde', 'amarelo', 'azul', 'azul', 'azul', 'branco')
print(cores[0])
print(cores[-1])
print(cores[1:3])
print(cores.index('amarelo'))
print(cores.count('azul'))
print(len(cores))

