from dotenv import load_dotenv, find_dotenv
import os, pprint
from pymongo import MongoClient

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://Group1:{password}@testdb.dhmeogy.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)

user_creds = client.user_creds
user_creds_collection = user_creds.user_creds_collection


def authenticate(email, passwd):
    user = user_creds_collection.find_one({"email": f"{email}"})
    print(user)
    if user["password"] == passwd:
        msg = [
            "name" , user["name"],
            "email", user["email"]
        ]
        return msg
    else:
        return False