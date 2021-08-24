import requests

def main():
    # Request da raiz:
    r = requests.get('http://localhost:8080')
    print(r.text)

    # Request passando usuario:
    r = requests.get('http://localhost:8080/usuarios/fulano')
    print(r.text)

    # Request POST:
    payload = {'usuario': 'beltrano', 'senha': 'xpto'}
    r = requests.post('http://localhost:8080/usuarios/incluir', data=payload)
    print(r.text)


if __name__=="__main__":
    main()