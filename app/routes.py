from flask import Flask, request, render_template, redirect, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Database setup (SQLite)
def init_db():
    conn = sqlite3.connect('app/database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    # Insert dummy data (only if the table is empty)
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        cursor.execute('INSERT INTO users (username, password) VALUES ("admin", "adminpass")')
        cursor.execute('INSERT INTO users (username, password) VALUES ("user", "userpass")')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Construire la requête SQL vulnérable
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    # Logs pour déboguer
    print(f"Received username: {username}")
    print(f"Received password: {password}")
    print(f"Executing query: {query}")
    
    # Exécuter la requête
    conn = sqlite3.connect('app/database.db')
    cursor = conn.cursor()
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()

    # Log le résultat de la requête
    print(f"Result from query: {user}")

    # Gestion des résultats
    if user:
        # Vérifiez si la requête a été faite normalement ou via injection SQL
        if username == user[1] and password == user[2]:  # Login légitime
            flash(f"Welcome {username}! You have successfully logged in.", "success")
            return render_template('real_dashboard.html', username=username)
        else:  # Injection SQL détectée
            flash("SQL Injection vulnerability exploited! You bypassed authentication.", "warning")
            return render_template('dashboard.html', username="Unknown (SQL Injected)")
    else:
        # Échec d'authentification
        flash("Login failed. Try again.", "danger")
        return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8080)
