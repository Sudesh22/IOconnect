import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

from time import time
from flask import Flask, jsonify, request
import sqlite3, socket
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get("/")
def home():
    return ("<h1>Hello</h1>")

@app.get("/decode")
def decode():
    data = request.get_json()
    encrypted = data["encrypted"]
    hash = data["hash"]
    decrypted = decrypt_AES_CBC_256("0123456789010123", encrypted)
    newHash = hashlib.sha256(decrypted.encode('utf-8')).hexdigest()
    print("encrypted data:",encrypted)
    print("decrypted data:",decrypted)
    # print("newHash is:",newHash)
    if newHash == hash:
        print("Security Status: Data received securely!!")
    else:
        print("Security Status: Data is tampered with!!")
    return ("received")

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


if __name__ == "__main__":
    app.debug=True
    IPAddr = socket.gethostbyname(socket.gethostname())  
    app.run(host=IPAddr, port=5000)