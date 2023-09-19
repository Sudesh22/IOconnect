from dotenv import load_dotenv, find_dotenv
import os, pprint
from pymongo import MongoClient
from random import randint

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://Group1:{password}@testdb.dhmeogy.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)

def log_to_database(data):
    encrypted_db = client.encrypted
    encrypted_collection = encrypted_db.encrypted_collection
    inserted_id = encrypted_collection.insert_one(data).inserted_id
    return ("Data inserted with id:", inserted_id)

def add_user(data):
    user_creds = client.user_creds
    user_creds_collection = user_creds.user_creds_collection
    token = randint(100000, 999999)
    data = {"name" :                 data["name"],
            "email":                 data["email"],
            "password":              data["password"],
            "Verification Token":    token,
            "Verification Status":   "Pending",
           }
    inserted_id = user_creds_collection.insert_one(data).inserted_id
    user = user_creds_collection.find_one({"email": f"{data['email']}"})
    msg = [
            "name" ,                 user["name"],
            "email",                 user["email"],
            "password",              user["password"],
            "Verification Token",    token,
            "Verification Status",   "Success",
        ]
    return data["name"]