from bd import nova_conexao

sql = "SELECT * FROM contatos WHERE nome like %s"

with nova_conexao() as conexao:
    nome = input('Contato a localizar: ')
    args = (f'%{nome}%',)

    cursor = conexao.cursor()
    # Nessa etapa é que se evita o sql Injection, passando os argumentos separados
    cursor.execute(sql, args)

    for x in cursor:
        print(x)