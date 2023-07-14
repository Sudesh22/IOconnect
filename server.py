import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

from time import time
from flask import Flask, jsonify, request, send_file
import sqlite3, socket, ast, csv, os
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get("/")
def home():
    return ("<h1>Hello</h1>")

@app.get("/decode")
def decode():
    Json = request.get_json()
    encrypted = Json["encrypted"]
    hash = Json["hash"]
    decrypted = decrypt_AES_CBC_256("0123456789010123", encrypted)
    if verify_hash(decrypted,hash):
        data = ast.literal_eval(decrypted)
        log_to_database(data)
        return jsonify({"status":"received"})
    else:
        return jsonify({"status":"Data compromised not saved to db"})

def decrypt_AES_CBC_256(key, ciphertext):
    key_bytes = key.encode('utf-8')
    ciphertext_bytes = b64decode(ciphertext)
    iv = ciphertext_bytes[:AES.block_size]
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    ciphertext_bytes = ciphertext_bytes[AES.block_size:]
    decrypted_bytes = cipher.decrypt(ciphertext_bytes)
    plaintext_bytes = unpad(decrypted_bytes, AES.block_size)
    plaintext = plaintext_bytes.decode('utf-8')
    return plaintext

def verify_hash(decrypted,hash):
    newHash = hashlib.sha256(decrypted.encode('utf-8')).hexdigest()
    if newHash == hash:
        print("Security Status: Data received securely!!")
    else:
        print("Security Status: Data is tampered with!!")

def log_to_database(data):
    sensor_id = data["sensor_id"]
    temperature = data["temperature"]
    humidity = data["humidity"]
    wind_speed = data["wind_speed"]
    location = data["location"]
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS DataLogging(
                    sensor_id int,
                    temperature int,
                    humidity int,
                    wind_speed int,
                    location text)
                """)
    c.execute("INSERT INTO DataLogging VALUES (?,?,?,?,?)", (sensor_id, temperature, humidity, wind_speed, location))
    conn.commit()
    conn.close()

@app.get("/get_csv")
def get_csv():
    csvWriter = csv.writer(open("output.csv", "a"))
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    rows = c.execute("SELECT * FROM DataLogging").fetchall()
    print(rows)
    for x in rows:
        csvWriter.writerow(x)    
    return send_file("output.csv")

if __name__ == "__main__":
    app.debug=True
    # IPAddr = socket.gethostbyname(socket.gethostname())  
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    IPAddr = s.getsockname()[0]
    app.run(host=IPAddr, port=5000)