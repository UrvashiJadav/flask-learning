from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/user',methods = ['POST']) #by default its GET, we are using POST because we want to take data and send response.
def user():
    data = request.get_json() #send req to take json data
    name = data.get('name') #gets name from json format

    if not name or not name.strip(): #if name is empty or space only, strip removes space
        response = {
            "status":"error",
            "message":"invalid name"
        } #resonse json format to send to js file
        return jsonify(response) #send response json format onlt if if condition is true
    
    msg = {
    "status": "success",
    "message": f"Hello {name}, request received successfully!"
    } 


    return jsonify(msg) #msf json format if its succesfull.

if __name__ == "__main__":
    app.run(debug=True)

