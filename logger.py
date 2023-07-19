from dotenv import load_dotenv, find_dotenv
import os, pprint
from pymongo import MongoClient

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://Group1:{password}@testdb.dhmeogy.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)

def log_to_database(data):
    encrypted_db = client.encrypted
    encrypted_collection = encrypted_db.encrypted_collection
    inserted_id = encrypted_collection.insert_one(data).inserted_id
    return ("Data inserted with id:", inserted_id)