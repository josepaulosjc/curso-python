#!python
# ----------- Exercício: Fibonacci com While Infinito e Brake----------- #


def fibonacci(quantidade):
    resultado = [0, 1]
    while True:
        # pegando o penultimo em diante e aplicando a lógica penultimo = ultimo
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
    return resultado


if __name__ == '__main__':
    # Listar os 20 primeiros número de fibonacci
    for fib in fibonacci(20):
        print(fib)
