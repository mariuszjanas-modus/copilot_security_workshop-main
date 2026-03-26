import sqlite3

from flask import Flask, jsonify
import random

def create_app():
    app = build_routes()
    app.run(debug=True)


def build_routes():

    app = Flask(__name__)

    @app.route('/secure_coding')
    def hello201():
        return "Welcome to the secure coding module!"

    @app.route('/secure_coding/random_boolean')
    def random_boolean():
        return jsonify({"value": random.choice([True, False])})

    @app.route('/secure_coding/cat')
    def cat():
        dummy_data = {
            "name": "Whiskers",
            "breed": "Siamese",
            "age": 3
        }
        response = jsonify(dummy_data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    
    
def get_db_connection():
    conn = sqlite3.connect('example.db')
    conn.row_factory = sqlite3.Row
    return conn
    
    return app

def get_db_connection():
    conn = sqlite3.connect('example.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/secure_coding/insecure_sql')
def insecure_sql():
    username = request.args.get('query')
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    result = cursor.execute(query, (username,)).fetchall()
    conn.close()
    users = [dict(row) for row in result]
    return jsonify(users)

@app.route('/secure_coding/insecure_xss')
def insecure_xss():
    user_input = request.args.get("input", "")
    return f"<h1>Hello, {user_input}</h1>"

@app.route('/secure_coding/hardcoded_login')
def hardcoded_login():
    username = request.args.get("username")
    password = request.args.get("password")
    
    if username == "admin" and password == "password123":
        return "Login Successful"
    return "Invalid credentials", 401

@app.route('/secure_coding/log_password')
def log_password():
    password = request.args.get("password")
    print(f"User entered password: {password}")
    return "Check server logs!"

@app.route('/secure_coding/read_file')
def read_file():
    filename = request.args.get("filename")
    with open(f"/var/www/data/{filename}", "r") as file:
        return file.read()