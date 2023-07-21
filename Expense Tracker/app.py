from flask import Flask, render_template, request, redirect, url_for
import database as db

app = Flask(__name__)

# Criando as tabelas no banco de dados ao iniciar a aplicação
db.create_tables()

@app.route('/')
def index():
    return render_template('index.html', expenses=get_expenses(), incomes=get_incomes())

@app.route('/add_expense', methods=['POST'])
def add_expense():
    amount = float(request.form['amount'])
    db.insert_expense(amount)
    return redirect(url_for('index'))

@app.route('/add_income', methods=['POST'])
def add_income():
    amount = float(request.form['amount'])
    db.insert_income(amount)
    return redirect(url_for('index'))

@app.route('/analytics')
def analytics():
    return render_template('analytics.html', expenses=get_expenses(), incomes=get_incomes())

def get_expenses():
    conn = db.sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute("SELECT amount FROM expenses")
    expenses = [row[0] for row in cursor.fetchall()]
    conn.close()
    return expenses

def get_incomes():
    conn = db.sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute("SELECT amount FROM incomes")
    incomes = [row[0] for row in cursor.fetchall()]
    conn.close()
    return incomes

if __name__ == '__main__':
    app.run(debug=True)