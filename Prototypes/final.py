from Crypto import Random
from Crypto.Cipher import AES
import base64
from pkcs7 import PKCS7Encoder
 # my custom settings

app_secrets = retrieve_settings(file_name='secrets');


def encrypt_data(text_data):
                    #limit to 16 bytes because my encryption key was too long
                    #yours could just be 'abcdefghwhatever' 
    encryption_key = app_secrets['ENCRYPTION_KEY'][:16]; 

    #convert to bytes. same as bytes(encryption_key, 'utf-8')
    encryption_key = str.encode(encryption_key); 
    
    #pad
    encoder = PKCS7Encoder();
    raw = encoder.encode(text_data) # Padding
    iv = Random.new().read(AES.block_size ) #AES.block_size defaults to 16

                                 # no need to set segment_size=BLAH
    cipher = AES.new( encryption_key, AES.MODE_CBC, iv ) 
    encrypted_text = base64.b64encode( iv + cipher.encrypt( str.encode(raw) ) ) 
    return encrypted_text;