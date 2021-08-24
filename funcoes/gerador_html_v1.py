#!python
# ---------- Parâmentros Posicionais ---------- #

def tag_bloco(texto, classe='sucess'):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == '__main__':
    # Teste (assertions)
    assert tag_bloco('incluído com sucesso!' ==
                     '<div class="sucesso">Incluído com sucesso!</div>')
    assert tag_bloco('Impossível excluir!', 'error' ==
                     '<div class="erro">Impossível excluir!</div>')
    print(tag_bloco('bloco'))
