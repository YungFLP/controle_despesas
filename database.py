import sqlite3

def conectar():
    conn = sqlite3.connect("despesas.db")
    return conn

def criar_tabela(): 
    conn = conectar() 
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS despesas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        valor REAL,
        categoria TEXT,
        descricao TEXT,
        data TEXT
    )
    """)

    conn.commit()
    conn.close()