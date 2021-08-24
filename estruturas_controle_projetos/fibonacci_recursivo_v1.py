#!python
# ----------- Exercício: Fibonacci com Recursivisidade ----------- #


def fibonacci(quantidade, sequencia=(0, 1)):
    # IMPORTANTE! : Condição de Parada
    if len(sequencia) == quantidade:
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    # Listar os 20 primeiros número de fibonacci
    for fib in fibonacci(20):
        print(fib)
