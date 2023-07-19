# Hash a single string with hashlib.sha256
import hashlib

a_string = 'The quick brown fox'

hashed_string = hashlib.sha256(a_string.encode('utf-8')).hexdigest()
print(hashed_string)