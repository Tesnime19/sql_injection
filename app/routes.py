from flask import Flask, request, render_template, redirect, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Database setup (SQLite)
def init_db():
    conn = sqlite3.connect('database.db')
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

    # Build SQL queries vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    # Logs for debug
    print(f"Received username: {username}")
    print(f"Received password: {password}")
    print(f"Executing query: {query}")
    
    # Execute the queries
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()

    # Log the queries of the request
    print(f"Result from query: {user}")

    # Result
    if user:
        flash(f"Welcome {username}! You have successfully logged in.", "success")
        return render_template('real_dashboard.html', username=username)
    else:
    # Échec de l'authentification
        flash("Login failed. Try again.", "danger")
        return redirect('/')


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8080)
