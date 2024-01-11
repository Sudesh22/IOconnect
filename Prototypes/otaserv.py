from Cryptography import decrypt_AES_CBC_256, verify_hash
from logger import log_to_database, log_alert, add_user, showData, isValid, saveOtp, changePass, showNotif, showConfig, showAnalysis, showHome
from Analytics.Vedantrik.Linear_Regression.linear_regression import linear_regression
from authenticate import authenticate, getUser
from verification import send_mail
from flask import Flask, jsonify, request, send_from_directory
from datetime import datetime
from flask_cors import CORS
from flask_caching import Cache 
from random import randint
from dotenv import load_dotenv, find_dotenv

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

import socket, ast, csv, os, sqlite3

app = Flask(__name__)
CORS(app)

@app.get("/")
def Home():
    json = request.get_json()
    print(json)
    return jsonify({"status" : "logged", "version" : 1.1})

@app.route('/update')
def download_file():
    return send_from_directory("frontend\\public\\UPDATE", "OTA_ver_0.1.ino.nodemcu.bin", as_attachment=True)

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

    # add_ip("frontend/src/App.js", 10, "    const baseUrl = \"" + "http://" + str(IPAddr) + ":" + str(port) + "\";\n")
    add_ip("frontend/package.json", 4, "  \"proxy\":\"" + "http://" + str(IPAddr) + ":" + str(port) + "\",\n")
    
    app.run(host="0.0.0.0", port=port)