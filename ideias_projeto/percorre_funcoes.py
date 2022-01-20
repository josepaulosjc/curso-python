def div(num):
    return 0

def mult(num):
    return num * 0

def soma(num):
    return num + 3

funcs = [div, soma, mult]
valor = 0

# MAP
result = map(lambda func: func(valor), funcs)
print('\nMAP:')
print(list(result))

# MAP COM FLTER
result =  filter(lambda valor: valor != 0, map(lambda func: func(valor), funcs))
print('\nMAP COM FLTER:')
print(list(result))

# GENERATOR
result = (func (valor) for func in funcs if func(valor) != 0)
print('\nGENERATOR:')
print(list(result))

# FLTER
funcao_recebida =  list(filter(lambda func: func(valor) if func(valor) != 0 else None, funcs))[0]
print('\nFLTER:')
print(funcao_recebida(valor))
