class Carro:
    def __init__(self, marca):
        self.marca = marca

    def str(self):
        return f'marca = {self.marca}'

    def dict(self):
        return {'marca': self.marca}


obj = Carro('Ford')
print(obj.dict())
