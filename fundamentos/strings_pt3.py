frase = 'Python eh uma linguagem excelente'

print('py' in frase) # False pois é 'Py' não 'py'
print('py' not in frase) # True
print('ing' in frase) # True

print(len(frase))
print(frase.lower())
print('py' in frase.lower()) # True

print(frase.upper())
print(frase.split()) # Por padrão usa espaços em branco

print(frase.split('a')) # 'Python eh um' , 'lingu' , 'gem excelente'

