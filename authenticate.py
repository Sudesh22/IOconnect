from dotenv import load_dotenv, find_dotenv
import os, pprint
from pymongo import MongoClient

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://Group1:{password}@testdb.dhmeogy.mongodb.net/"

client = MongoClient(connection_string)

user_creds = client.user_creds
user_creds_collection = user_creds.user_creds_collection

def authenticate(email, passwd, access_token):
    user = user_creds_collection.find_one({"email": f"{email}"})
    # print(user) 
    print(user["password"])
    if user["password"] == passwd:
        # msg = [user["name"], user["email"]]
        msg = {
            "status" : "Succesful",
            "access_token" : access_token,
            "email" : user["email"], 
            "user" : user["name"],
            }
        print("True")
        return msg
    else:
        print("False")
        return False
    
def get_token(email):
    user = user_creds_collection.find_one({"email": f"{email}"})
    print(user)
    return user["Verification Token"]

def check_token(username,token):
    user = user_creds_collection.find_one({"email": f"{email}"})
    print(user)
    return user["Verification Token"]
