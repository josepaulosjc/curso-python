nome = 'Saulo Lopes'
print(nome[0])  # Imprime 'S'

#nome[0] = 'P' # Não Funciona 'A STRING É IMUTÁVEL'

# texto = 'marca d'agua'  # Erro de Aspas Simples

# Formas para Resolver
texto = "Marca d' agua"
print(texto)

texto = 'Marca d\' agua'
print(texto)

texto = 'Posso colocar "aspas duplas" dentro das simples'
print(texto)

texto = '''Texto 
com
multiplas
linhas
'''
print(texto)

texto = "Linha unica \
com quebra de \
linha no codigo"
print(texto)

texto = 'Texto com escape \n com quebra de \n linha'
print(texto)
