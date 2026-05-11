import sqlite3
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

connection = sqlite3.connect('database.db')
cursor = connection.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS users ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT ,username TEXT, password TEXT )''')
connection.commit()
connection.close()

@app.route('/',methods=['GET'])
def rentem():
    return render_template('register.html')

@app.route('/LOGIN',methods=['GET'])
def login_page():
    return render_template('login.html')

@app.route('/home',methods=['GET'])
def home_page():
    return render_template('home.html')

@app.route('/register', methods=['POST'])
def register():

    reqdata = request.get_json()

    name = reqdata.get("name")
    username = reqdata.get("username")
    password = reqdata.get("password")

    if not name or not name.strip():
        response = {
            "status": "error",
            "message": "Invalid Name"
        }
        return jsonify(response)

    if not username or not username.strip():
        response = {
            "status": "error",
            "message": "Invalid Username"
        }
        return jsonify(response)

    if not password or not password.strip():
        response = {
            "status": "error",
            "message": "Invalid Password"
        }
        return jsonify(response)

    response = {
        "status": "success",
        "message": f"Hello {name}, You're Successfully REGISTERED!!"
    }

    return jsonify(response)

@app.route('/login', methods=['POST'])
def login():

    reqdata = request.get_json()

    username = reqdata.get("username")
    password = reqdata.get("password")

    if not username or not username.strip():
        response = {
            "status": "error",
            "message": "Invalid Username"
        }
        return jsonify(response)

    if not password or not password.strip():
        response = {
            "status": "error",
            "message": "Invalid Password"
        }
        return jsonify(response)
    
    response = {
        "status": "success",
        "message": f"Hello {username}, You're Successfully REGISTERED!!"
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)