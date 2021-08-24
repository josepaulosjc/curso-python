# ---------- Packing Nomeado: KWARGS (Key Words Args)---------- #

def resultado_f1(**podium):  # **podium = dicionario
    for posicao, piloto in podium.items():
        print(f'{posicao} --> {piloto}')


if __name__ == '__main__':
    resultado_f1(primeiro='L. Hamilton',
                 segundo='M. Vestappen',
                 terceiro='S. Vettel')
