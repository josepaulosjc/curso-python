#!python
# ----------- Exercício: Fibonacci com For e Variável não usada '_' ----------- #


def fibonacci(quantidade):
    resultado = [0, 1]
    for _ in range(2, quantidade):  # 2 pq já temos dois elementos
        # pegando o penultimo em diante e aplicando a lógica penultimo = ultimo
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    # Listar os 20 primeiros número de fibonacci
    for fib in fibonacci(20):
        print(fib)
