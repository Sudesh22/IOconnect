from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
import hashlib

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
        return True
    else:
        print("Security Status: Data is tampered with!!")
        return False

# text = decrypt_AES_CBC_256("0000000000000000", "WTaZQrgOPjp6TgUw/RogmjsLmI/1qUVxwE7LWkldP2kOYjp1ngPZKMO8Hu5qE+M62iL/3PxAijfkTK3qbdAyjmFaUnTjxcREA/w8IrodilQ=")
# print(text)
# dict_ = {"Sensor_data" : {"a":"b"}, "Device_data" : {"c":"d"}}
# print(dict_["Sensor_data"])