from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
from dotenv import load_dotenv, find_dotenv
import hashlib, hmac, os

load_dotenv(find_dotenv())
hs_key = os.environ.get("HMACSHA256_KEY").encode()

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
    newHash = hmac.new(hs_key, decrypted.encode(), digestmod='SHA256').hexdigest()
    if newHash == hash:
        print("Security Status: Data received securely!!")
        return True
    else:
        print("Security Status: Data is tampered with!!")
        return False