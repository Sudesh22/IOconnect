from Cryptography import decrypt_AES_CBC_256, verify_hash
from logger import log_to_database, add_user
from authenticate import authenticate,check_token
from verification import send_mail
from flask import Flask, jsonify, request
from datetime import datetime
from flask_cors import CORS

import socket, ast, csv, os, sqlite3

app = Flask(__name__)
CORS(app)

@app.get("/")
def home():
    return ("<h1>Hello</h1>")

@app.post("/decode")
def decode():
    Json = request.get_json()
    encrypted = Json["encrypted"]
    hash = Json["hash"]
    decrypted = decrypt_AES_CBC_256("0123456789010123", encrypted)
    if verify_hash(decrypted,hash):
        data = ast.literal_eval(decrypted)
        log_to_database(Json)
        return jsonify({"status":"received"})
    else:
        return jsonify({"status":"Data compromised not saved to db"})
    
@app.post("/signin")
def signIn():
    data = request.get_json()
    email = data["email"]
    password = data["password"]
    print(email,password)
    if authenticate(email, password):
        # return (authenticate(email, password))
        return jsonify({"status": "Error logging in"})
    else:
        return jsonify({"status": "Error logging in"})

@app.post("/dashboard")
def dashboard():
    device_id = 2
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    Data = c.execute(
        "SELECT * FROM DataLogging WHERE Device_Id = ? ORDER BY Time DESC limit 7", (device_id,)).fetchall()
    conn.close()
    return jsonify(Data)

@app.post("/signup")
def signUp():
    new_user = request.get_json()
    print(new_user)
    username = add_user(new_user)
    send_mail(new_user["email"])
    return jsonify({"Status" : "Verification pending", "username" : username})

@app.post("/changePass")
def verify():
    response = request.get_json()
    print(response)
    # check_token(response["name"],response["otp"])
    send_mail(response["signUpEmail"])
    return jsonify({"Status" : "Mail sent succesfully"})

if __name__ == "__main__":
    app.debug=True
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    IPAddr = s.getsockname()[0]
    port = 8081

    def add_ip(file_path, line_num, text):
        lines = open(file_path, 'r').readlines()
        lines[line_num] = text
        out = open(file_path, 'w')
        out.writelines(lines)
        out.close()

    add_ip("frontend/src/App.js", 9, "    const baseUrl = \"" + "http://" + str(IPAddr) + ":" + str(port) + "\";\n")
    add_ip("frontend/package.json", 4, "  \"proxy\":\"" + "http://" + str(IPAddr) + ":" + str(port) + "\",\n")
    
    app.run(host=IPAddr, port=port)