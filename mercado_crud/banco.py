import sqlite3

def conectar():
    return sqlite3.connect("produtos.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        quantidade INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()
    
def cadastrar(nome, preco, quantidade):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO produtos(nome, preco, quantidade) VALUES (?, ?, ?)",
        (nome, preco, quantidade)
    )

    conn.commit()
    conn.close()
    
    
def listar():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM produtos")

    dados = cursor.fetchall()

    conn.close()

    return dados


def atualizar(id_produto, nome, preco, quantidade):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE produtos
    SET nome = ?, preco = ?, quantidade = ?
    WHERE id = ?
    """, (nome, preco, quantidade, id_produto))

    conn.commit()
    conn.close()
    
    

def excluir(id_produto):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM produtos WHERE id = ?",
        (id_produto,)
    )

    conn.commit()
    conn.close()
    
