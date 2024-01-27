# Import the required modules
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
import hashlib

# Define the encryption function
def encrypt_AES_CBC_256(key, message):
    key_bytes = key.encode('utf-8')
    message_bytes = message.encode('utf-8')
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    padded_message = pad(message_bytes, AES.block_size)
    ciphertext_bytes = cipher.encrypt(padded_message)
    ciphertext = b64encode(iv + ciphertext_bytes).decode('utf-8')
    return ciphertext

# Set the 12-bit key and plaintext message
key = '0000000000000000'
message = "{'Device_Id': 1, 'Temperature1': 29.56, 'Temperature2': 30.19, 'Status': 'Working', 'Date': '2024-02-01', 'Time': '00:00:00'}"

# Encrypt the message
encrypted_message = encrypt_AES_CBC_256(key, message)

# Create a hash of the data to check 
# if the data is safely transferred
hashed_string = hashlib.sha256(message.encode('utf-8')).hexdigest()


# Print the original and decrypted messages
print('Encrypted Message:', encrypted_message)
print('Hashed Message:', hashed_string)