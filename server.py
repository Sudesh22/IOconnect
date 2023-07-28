from Cryptography import decrypt_AES_CBC_256, verify_hash
from logger import log_to_database, add_user
from authenticate import authenticate
from verification import send_mail
from flask import Flask, jsonify, request
from datetime import datetime
from flask_cors import CORS

import socket, ast, csv, os

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
    if authenticate(email, password):
        return (authenticate(email, password))
    else:
        return jsonify({"status": "Error logging in"})

@app.post("/signup")
def signUp():
    new_user = request.get_json()
    print(new_user)
    # send_mail(new_user["email"])
    add_user(new_user)
    return jsonify({"Status" : "Verification pending"})

@app.post("/verify")
def verify():
    otp = request.get_json()
    print(otp)
    return jsonify({"Status" : "User added succesfully"})

if __name__ == "__main__":
    app.debug=True
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    IPAddr = s.getsockname()[0]
    port = 5000

    def add_ip(file_path, line_num, text):
        lines = open(file_path, 'r').readlines()
        lines[line_num] = text
        out = open(file_path, 'w')
        out.writelines(lines)
        out.close()

    add_ip("frontend/src/App.js", 9, "    const baseUrl = \"" + "http://" + str(IPAddr) + ":" + str(port) + "\";\n")
    add_ip("frontend/package.json", 4, "  \"proxy\":\"" + "http://" + str(IPAddr) + ":" + str(port) + "\",\n")
    
    app.run(host=IPAddr, port=port, ssl_context='adhoc')