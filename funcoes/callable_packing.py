#!python
# --------- PACKING e UNPACKING com Tuplas --------- #


# Fez Packing linha 20 - calc_preco_final(preco_final, imposto_y, True, 1.5)
def calc_preco_final(preco_bruto, calc_imposto, *params):
    if callable(calc_imposto):
        # Faz Unpacking linha 12 - imposto_y(explosivo, fator_mult=1)
        return preco_bruto + preco_bruto * calc_imposto(*params)


def imposto_x(importado):
    return 0.22 if importado else 0.13


def imposto_y(explosivo, fator_mult=1):
    return 0.11 * fator_mult if explosivo else 0


if __name__ == '__main__':
    preco_bruto = 134.90
    preco_final = calc_preco_final(preco_bruto, imposto_x, True)
    preco_final = calc_preco_final(preco_final, imposto_y, True, 1.5)
    print('O preco final do produto sera: R$ {:.2f}'.format(preco_final))
