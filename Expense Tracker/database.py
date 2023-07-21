import sqlite3

DB_NAME = 'finance.db'

def create_tables():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Criando a tabela de despesas
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      amount REAL NOT NULL
                      )''')

    # Criando a tabela de receitas (rendimentos)
    cursor.execute('''CREATE TABLE IF NOT EXISTS incomes (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      amount REAL NOT NULL
                      )''')

    conn.commit()
    conn.close()

def insert_expense(amount):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (amount) VALUES (?)", (amount,))
    conn.commit()
    conn.close()

def insert_income(amount):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO incomes (amount) VALUES (?)", (amount,))
    conn.commit()
    conn.close()