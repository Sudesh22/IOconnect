# Import the required modules
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

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

# Define the decryption function
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

# Set the 256-bit key and plaintext message
key = '1234567890101234'
message = 'This is a secret message that needs to be encrypted.'

# Encrypt the message
encrypted_message = encrypt_AES_CBC_256(key, message)

# Decrypt the message
decrypted_message = decrypt_AES_CBC_256(key, encrypted_message)

# Print the original and decrypted messages
print('Original Message:', message)
print('Encrypted Message:', encrypted_message)
print('Decrypted Message:', decrypted_message)