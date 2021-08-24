class Carro():
    def __init__(self, vel_max):
        self.vel_max = vel_max  # Velocidade Máxima
        self.vel_atual = 0      # Velocidade Inicial

    def acelerar(self, delta=5):
        maxima = self.vel_max
        nova = self.vel_atual + delta
        # Se a velocidade atual acabou de ultrapassar a velocidade maxima então colocque a velocidade maxima
        self.vel_atual = nova if nova <= maxima else maxima
        return f'vruumm...{self.vel_atual}'

    def frear(self, delta=5):
        minima = 0
        nova = self.vel_atual - delta
        self.vel_atual = nova if nova >= minima else minima
        return self.vel_atual


if __name__ == '__main__':
    c1 = Carro(180)     # 180 Velocidade Máxima

    for _ in range(25):
        print(c1.acelerar(8))  # Padrão = 5, subir de 8  em 8

    for _ in range(10):
        print(c1.frear(delta=20))  # Decrementar de 20 em 20 até 0
