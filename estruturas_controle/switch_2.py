def get_dia_uteis(dia):
    dias = {
        1: 'Domingo, Final de Semana',
        2: 'Segunda, Dia de Semana',
        3: 'Terca, Dia de Semana',
        4: 'Quarta, Dia de Semana',
        5: 'Quinta, Dia de Semana',
        6: 'Sexta, Dia de Semana',
        7: 'Sabado, Final de Semana'
    }

    if dia in [1, 7]:
        return dias.get(dia)
    else:
        return dias.get(dia, ' ** Dia invalido **')


if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_dia_uteis(dia)}')
