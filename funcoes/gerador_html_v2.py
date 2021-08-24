#!python
# ---------- Parâmentros Nomeados ---------- #

def tag_bloco(texto, classe='sucess', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'


if __name__ == '__main__':
    # Teste (assertions)
    assert tag_bloco('incluído com sucesso!' ==
                     '<div class="sucesso">Incluído com sucesso!</div>')
    assert tag_bloco('Impossível excluir!', 'error' ==
                     '<div class="erro">Impossível excluir!</div>')
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', 'info', True))
    print(tag_bloco(inline=True, texto='inline'))
    print(tag_bloco('falhou', classe='error'))
