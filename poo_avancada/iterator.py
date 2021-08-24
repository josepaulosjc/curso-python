# ---------- Aplicando outra forma de iteração ---------- #

class RGB:
    def __init__(self):
        # retira os elementos de tras para frente
        self.cores = ['red', 'green', 'blue'][::-1]

    # Iterando com __iter__
    def __iter__(self):
        return self

    # Processando iterator
    def __next__(self):
        try:
            return self.cores.pop()
        except IndexError:
            raise StopIteration()


if __name__ == '__main__':
    cores = RGB()
    print(next(cores))
    print(next(cores))
    print(next(cores))

    try:
        print(next(cores))
    except StopIteration:
        print('Acabou!')

# Iterando com __iter__
for cor in RGB():
    print(cor)
