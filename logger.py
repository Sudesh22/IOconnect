from dotenv import load_dotenv, find_dotenv
import os, pprint, pymongo
from pymongo import MongoClient
from datetime import datetime

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://Group1:{password}@testdb.dhmeogy.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)


def log_to_database(data):
    encrypted_db = client.encrypted
    encrypted_collection = encrypted_db.encrypted_collection
    inserted_id = encrypted_collection.insert_one(data).inserted_id
    return ("Data inserted with id:", inserted_id)

def add_user(data,access_token):
    user_creds = client.user_creds
    user_creds_collection = user_creds.user_creds_collection
    
    db_name = str(data["name"])+"@"+str(data["email"])
    data = {"name" :                 data["name"],
            "email":                 data["email"],
            "password":              data["password"],
           } 
    inserted_id = user_creds_collection.insert_one(data).inserted_id
    user = user_creds_collection.find_one({"email": f"{data['email']}"})
    # msg = [
    #         "name" ,                 user["name"],
    #         "email",                 user["email"],
    #         "password",              user["password"],
    #         "Verification Token",    token,
    #         "Verification Status",   "Success",
    #       ]
    access_token_db = client.access_token_db
    access_token_db_collection = access_token_db.access_token_db_collection
    data_db = {"access_token"       : access_token, 
               "db_name"            : data["name"],
               "dash_collection"    : db_name,
               "config_collection"  : db_config,
               "notif_collection"   : db_notif,
               "predict_collection" : db_predict,
               } 
    access_token_db_collection.insert_one(data_db)
    db = client[data["name"]]
    db.create_collection(db_name)
    db.create_collection(db_name)
    db.create_collection(db_name)
    return data["name"]

def showData(access_token):
    access_token_db = client.access_token_db
    access_token_db_collection = access_token_db.access_token_db_collection
    entry = access_token_db_collection.find_one({"access_token": f"{access_token}"})
    db_name = entry["db_name"]
    db_collection = entry["db_collection"]
    db = client[db_name]
    data = db.get_collection(db_collection).find({},{"_id" : 0}).sort('_id', pymongo.DESCENDING).limit(7)
    # print(type(data))
    DataList = []
    for d in data:
        DataList.append(tuple(d.values()))
        # print(tuple(d))

    # print(type(DataList))
    return DataList

def checkOtp(otp,access_token):
    access_token_db = client.access_token_db
    access_token_db_collection = access_token_db.access_token_db_collection
    entry = access_token_db_collection.find_one({"access_token": f"{access_token}"})
    username = entry["db_name"]
    change_pass_db = client.change_pass_db
    change_pass_db_collection = change_pass_db.change_pass_db_collection
    entry = {"access_token" : access_token, 
            "username" : username,
            "otp" : otp,
            "timestamp": datetime.now().strftime("/%d/%m/%Y, %H:%M:%S")
            } 
    change_pass_db_collection.insert_one(entry)
    user_creds = client.user_creds
    user_creds_collection = user_creds.user_creds_collection
    user_creds_collection.update_one({"name":f"{username}"},{"$set":{"password":f"{access_token}"}})