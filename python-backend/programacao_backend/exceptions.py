try:
    arquivo = open('arquivo.txt')
    print(arquivo.read())
except FileNotFoundError as e:
    print('Arquivo Inexistente')
    # raise --> Não Executa finally
finally:
    print('Fim!')
