from Cryptography import decrypt_AES_CBC_256, verify_hash
from logger import log_to_database
from flask import Flask, jsonify, request, send_file
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

# @app.get("/get_csv")
# def get_csv():
#     csvWriter = csv.writer(open("output.csv", "a"))
#     conn = sqlite3.connect('test.db')
#     c = conn.cursor()
#     rows = c.execute("SELECT * FROM DataLogging").fetchall()
#     print(rows)
#     for x in rows:
#         csvWriter.writerow(x)    
#     return send_file("output.csv")

if __name__ == "__main__":
    app.debug=True
    # IPAddr = socket.gethostbyname(socket.gethostname())  
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    IPAddr = s.getsockname()[0]
    app.run(host=IPAddr, port=5000)