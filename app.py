from flask import Flask

app = Flask(__name__)

@app.route('/user',methods = ['GET'])

def user():
    return "hello world"

if __name__ == "__main__": #ledt side variable and right side string so do '' otherwise it will treate __main__ as var.
    app.run(debug=True)




