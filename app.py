from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])
def rentem():
    return render_template('register.html')

@app.route('/user', methods=['POST'])
def user():

    data = request.get_json()

    name = data.get('name')
    email = data.get('email')

    if not name or not name.strip():
        response = {
            "status": "error",
            "message": "Invalid Name"
        }
        return jsonify(response)

    if not email or not email.strip():
        response = {
            "status": "error",
            "message": "Invalid Email"
        }
        return jsonify(response)

    response = {
        "status": "success",
        "message": f"Hello {name}, request received successfully!"
    }

    return jsonify(response)


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
        "message": f"Hello {username}, You're Successfully LOGGED IN!!"
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)