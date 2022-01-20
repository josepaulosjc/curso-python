from datetime import datetime

def calcular_tempo():
    inicio_metodo = datetime.now(tz=None)
    x = 3
    y = 5
    z = x + y + y * y + x
    fim_metodo = datetime.now(tz=None)
    return print(f"Tempo exec. calcular_tempo()\
        {(fim_metodo - inicio_metodo).total_seconds()}")


if __name__=='__main__':
    calcular_tempo()