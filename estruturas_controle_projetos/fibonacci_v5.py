#!python
# ----------- Exercício: Fibonacci com Função Sum() ----------- #


def fibonacci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        # pegando o penultimo em diante e aplicando a lógica penultimo = ultimo
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(20000):
        print(fib)
