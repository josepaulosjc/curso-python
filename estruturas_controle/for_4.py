'''
for i in range(1, 11):
    if i == 6:
        break
    print(i)
else:
    print('Fim!')
'''
from random import randint


def sortear_dado():
    return randint(1, 6)


for i in range(1, 7):
    if i % 2 == 1:
        continue
    elif i == sortear_dado():
        print('ACERTOU', i)
        break
else:
    print('Nao acertou o numero')
