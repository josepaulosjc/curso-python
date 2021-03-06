#!python
# ---------- Packing ---------- #

def tag_bloco(conteudo, *args, classe='sucess', inline=False):
    tag = 'span' if inline else 'div'
    # Passando o conteudo se ele não for uma funcao, se for ele passa o conteudo com os argumentos.
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'


def tag_lista(*itens):
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    # Teste (assertions)
    assert tag_bloco('incluído com sucesso!' ==
                     '<div class="sucesso">Incluído com sucesso!</div>')
    assert tag_bloco('Impossível excluir!', 'error' ==
                     '<div class="erro">Impossível excluir!</div>')
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', 'info', True))
    print(tag_bloco(inline=True, conteudo='inline'))
    print(tag_bloco(conteudo='falhou', classe='error'))

    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))
    print(tag_bloco(tag_lista('Sabado', 'Domingo'), classe='info', inline=True))
