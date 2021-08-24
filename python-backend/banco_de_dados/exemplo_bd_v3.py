import psycopg2

DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "postgres"


print('Conectando ao Banco...')
try:
    con = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

except:
    raise

# ---------- UPDATE --------- #
query = "update account set username = 'alex' where user_id=1"

cursor = con.cursor()     # Realiza conexão
cursor.execute(query)     # Executa Query
con.commit()              # Aprova modificacao
con.close()               # Fecha Conexao
print('Conexao Encerrada!')
