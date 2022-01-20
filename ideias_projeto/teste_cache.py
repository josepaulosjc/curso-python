import requests

def consulta():
    resultado = requests.get('http://files.cod3r.com.br/curso-js/funcionarios.json')
    return resultado

if __name__=='__main__':
    res = consulta()
    print(dir(res))
    print('Valor da cache: ' + str(res.status_code))