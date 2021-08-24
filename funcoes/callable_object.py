#!python
class Potencia:
    # Calcula potência especifica, init é o costrutor
    def __init__(self, expoente):
        self.expoente = expoente

    # Metodo que será chamado
    def __call__(self, base):
        return base ** self.expoente


if __name__ == '__main__':
    quadrado = Potencia(2)  # Passa o valor de init sendo 2
    cubo = Potencia(3)

    if callable(quadrado) and callable(cubo):
        print(f'3**2 => {quadrado(3)}')  # Passa o valor de Call sendo 3
        print(f'5**3 => {cubo(5)}')
        print(f'2**4 => {Potencia(4)(2)}')
