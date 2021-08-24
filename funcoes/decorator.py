#!python
def log(function):  # É passado a função como parâmento soma(5, 7)
    def decorator(*args, **kwargs):  # É separado os argumentos com base nos parâmetros
        print(f'Inicio da chamada da funcao {function.__name__}')
        print(f'args: {args}')  # Argumentos Posicionais
        print(f'kwargs: {kwargs}')  # Argumentos Nomeados
        # Chama a função e armazena o retorno
        resultado = function(*args, **kwargs)
        print(f'Resultado da chamada: {resultado} ')
        return resultado  # Retorna resultado
    return decorator  # Retorna Decorator


@log
def soma(x, y):
    return x + y


@log
def sub(x, y):
    return x - y


if __name__ == '__main__':
    print(soma(5, 7))
    print(sub(5, y=7))
