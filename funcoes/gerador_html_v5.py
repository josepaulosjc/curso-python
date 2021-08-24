#!python
# ---------- Packing e Unpacking Nomeado ---------- #

# Filtros de Suporte...bloco_atrs --> PERMITE OS ATRIBUTOS -----> ('bloco_accesskey', 'bloco_id')
bloco_atrs = ('bloco_accesskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_style')


def get_atrs(informados, suportados):
    # Faz separação dos 'novos_atrs', remove o 'bloco_'  do 'bloco_id'
    # Só gerará o atributo, se a chave estiver dentro de suportados
    return ' '.join(f'{k.split("_")[-1]}="{v}"'
                    for k, v in informados.items() if k in suportados)


def tag_bloco(conteudo, *args, classe='sucess', inline=False, **novos_atrs):
    tag = 'span' if inline else 'div'
    # Passando o conteudo se ele não for uma funcao, se for ele passa o conteudo com os argumentos.
    html = conteudo if not callable(
        conteudo) else conteudo(*args, **novos_atrs)
    atributos = get_atrs(novos_atrs, bloco_atrs)
    return f'<{tag} {atributos} class="{classe}">{html}</{tag}>'


def tag_lista(*itens, **novos_atrs):
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul {get_atrs(novos_atrs, ul_atrs)}>{lista}</ul>'


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

    # 'tag_lista' = é um callable, bloco_accesskey, bloco_id, ul_id = **novos_atrs
    print(tag_bloco(tag_lista, 'Item 1', 'Item 2', classe='info',
                    bloco_accesskey='m', bloco_id='conteudo', ul_id='lista', ul_style='color:red'))
