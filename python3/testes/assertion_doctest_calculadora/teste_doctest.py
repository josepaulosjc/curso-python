def soma(x, y):
    # Testando através de comnetarios de documentação
    ''' Soma x e y
    >>> soma(10, 20)
    30

    >>> soma(-10, 20)
    10
    '''
    # Testando uma Exceção (Não Precisa Escrever a Exceção toda: 'INICIO...FIM')
    '''
    >>> soma('10', 20)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float
    '''
    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(y, (int, float)), 'y precisa ser int ou float'
    return x + y

def sub(x, y):
    '''
    >>> sub(10, 5)
    5

    >>> sub('10', 5)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float
    '''
    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(y, (int, float)), 'y precisa ser int ou float'
    return x - y


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)