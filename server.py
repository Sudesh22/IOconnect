from Cryptography import decrypt_AES_CBC_256, verify_hash
from logger import log_to_database, add_user, showData, isValid, saveOtp, changePass
from authenticate import authenticate, getUser
from verification import send_mail
from flask import Flask, jsonify, request
from datetime import datetime
from flask_cors import CORS
from flask_caching import Cache 
from random import randint

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

import socket, ast, csv, os, sqlite3

app = Flask(__name__)
CORS(app)

app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)

cache=Cache(app,config={'CACHE_TYPE': 'simple'})
cache_timeout = 60

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
# @cache.cached(timeout=cache_timeout) 
def signIn():
    try :
        data = request.get_json()
        email = data["email"]
        password = data["password"]
        # print(email,password) 
        access_token = create_access_token(identity=email)
        exists = authenticate(email, password, access_token)
        if exists:
            return (exists)
        else:
            return jsonify({"status": "Error logging in"})
    except:
        return jsonify({"status": "Error logging in"})

@app.post("/dashboard")
# @cache.cached(timeout=cache_timeout) 
# @jwt_required()
def dashboard():
    data = request.get_json()
    access_token = data["access_token"]
    payload = showData(access_token)
    return jsonify(payload)

@app.post("/signup")
@cache.cached(timeout=cache_timeout) 
def signUp():
    new_user = request.get_json()
    print(new_user)
    email = new_user["email"]
    access_token = create_access_token(identity=email)
    username = add_user(new_user,access_token)
    # send_mail(new_user["email"])
    return jsonify({"Status" : "Verification pending", "username" : username, "access_token" : access_token})

@app.post("/changePass")
# @cache.cached(timeout=cache_timeout) 
def verify():
    response = request.get_json()
    print(response)
    # check_token(response["name"],response["otp"])
    otp = randint(1000,9999)
    access_token = response["access_token"]
    name, email = getUser(access_token)
    send_mail(name, email, "resetPass", otp)
    saveOtp(access_token, otp)
    return jsonify({"Status" : "Mail sent succesfully"})

@app.post("/getOtp")
def getOtp():
    response = request.get_json()
    print(response)
    access_token = response["access_token"]
    otp = response["otp"]
    if isValid(access_token, otp):
        return jsonify({"Status" : "Success"})
    else:
        return jsonify({"Status" : "Failed"})

@app.post("/newPass")
def newPass():
    response = request.get_json()
    print(response)
    changePass(response["access_token"],response["password"])
    return jsonify({"Status" : "Password changed succeessfully"})

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

    add_ip("frontend/src/App.js", 10, "    const baseUrl = \"" + "http://" + str(IPAddr) + ":" + str(port) + "\";\n")
    add_ip("frontend/package.json", 4, "  \"proxy\":\"" + "http://" + str(IPAddr) + ":" + str(port) + "\",\n")
    
    app.run(host=IPAddr, port=port)