from database import conectar
from datetime import datetime


def adicionar_despesa(valor, categoria, descricao):
    conn = conectar()
    cursor = conn.cursor()

    data = datetime.now().strftime("%d/%m/%Y")

    cursor.execute("""
        INSERT INTO despesas (valor, categoria, descricao, data)
        VALUES (?, ?, ?, ?)
    """, (valor, categoria, descricao, data))

    conn.commit()
    conn.close()


def listar_despesas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM despesas")
    despesas = cursor.fetchall()

    conn.close()

    return despesas

def excluir_despesa(despesa_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM despesas WHERE id = ?", (despesa_id,))
    conn.commit()
    conn.close()

