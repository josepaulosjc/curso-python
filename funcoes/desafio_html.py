#!python

# ---------- DESAFIO HTML ---------- #

''' ---------- SAÍDA ESPERADA ----------
    <p class="alert">
    <span>Curso de Python 3, por </span><strong id="jf">Juracy Filho</strong>
    <span> e </span><strong id="ll">Leonardo Leitao</strong><span >.</span></p> 
'''


def tag(tag, *args, **kwargs):
    if 'html_class' in kwargs:
        # Substitui 'html_class' por 'class'
        kwargs['class'] = kwargs.pop('html_class')
    # Criando atributos, percorrendo kwargs e fazendo join
    attrs = ' '.join(f'{k}="{v}"' for k, v in kwargs.items())
    # Criando o conteudo da Tag retornando tudo formatado
    inner = ''.join(args)
    return f'<{tag}{attrs}>{inner}</{tag}>'


if __name__ == '__main__':
    print(tag('p',
              tag('span', 'Curso de Python 3, por '),
              tag('strong', 'Juracy Filho', id='jf'),
              tag('span', ' e '),
              tag('strong', 'Leonardo Leitão', id='ll'),
              tag('span', '.'),
              html_class='alert')
          )
