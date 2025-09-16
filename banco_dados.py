import sqlite3

conexao = sqlite3.connect('meu_banco.db')
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS cliente (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        email TEXT,
        data_nascimento DATE
)
""")

conexao.commit()
conexao.close()