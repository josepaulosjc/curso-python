'''
1 - Receber um número inteiro
2 - Saber se o número é múltiplo de 3 e 5:
    Bacon com Ovos
3 - Se multiplo somente de 3:
    Bacom
4 - Se multiplo somente de 5:
    Ovos
5 - Se não é multiplo de nenhum então:
    Passa fome
'''
def bacon_com_ovos(n):
    assert isinstance(n, int), 'n deve ser int'

    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon com ovos'
        
    elif n % 3 == 0:
        return 'Bacon'

    elif n % 5 == 0:
        return 'Ovos'
    
    return 'Passar fome'