from dotenv import load_dotenv, find_dotenv
import os, pprint, pymongo
from pymongo import MongoClient
from datetime import datetime,timedelta

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
    
    db_name = str(data["name"])+"@dash"
    db_config = str(data["name"])+"@config"
    db_notif = str(data["name"])+"@notif"
    db_predict = str(data["name"])+"@predict"
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
    now = datetime.strptime(datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),"%d/%m/%Y, %H:%M:%S")
    data_db = {"access_token"       : access_token, 
               "at_issued_at"       : now,
               "at_expires_at"      : now + timedelta(days=1, hours=12),
               "db_name"            : data["name"],
               "dash_collection"    : db_name,
               "config_collection"  : db_config,
               "notif_collection"   : db_notif,
               "predict_collection" : db_predict,
               } 
    access_token_db_collection.insert_one(data_db)
    db = client[data["name"]]
    db.create_collection(db_name)
    db.create_collection(db_config)
    db.create_collection(db_notif)
    db.create_collection(db_predict)
    return data["name"]

def showData(access_token):
    access_token_db = client.access_token_db
    access_token_db_collection = access_token_db.access_token_db_collection
    entry = access_token_db_collection.find_one({"access_token": f"{access_token}"})
    db_name = entry["db_name"]
    db_collection = entry["dash_collection"]
    db = client[db_name]
    data = db.get_collection(db_collection).find({},{"_id" : 0}).sort('_id', pymongo.DESCENDING).limit(7)
    # print(type(data))
    DataList = []
    for d in data:
        DataList.append(tuple(d.values()))
        # print(tuple(d))

    # print(type(DataList))
    return DataList

def saveOtp(access_token,otp):
    change_pass_db = client.change_pass_db
    change_pass_db_collection = change_pass_db.change_pass_db_collection
    now = datetime.strptime(datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),"%d/%m/%Y, %H:%M:%S")
    data = {
            "access_token" : access_token,
            "requested_at" : now,
            "expires_at"   : now + timedelta(minutes=10),
            "processed_at" : "",
            "otp"          : otp,
           }
    change_pass_db_collection.insert_one(data)

def isValid(access_token, otp):
    change_pass_db = client.change_pass_db
    change_pass_db_collection = change_pass_db.change_pass_db_collection
    entry = change_pass_db_collection.find_one({"access_token": f"{access_token}"})
    if entry["expires_at"] > datetime.now():
        change_pass_db_collection.update_one({"access_token":f"{access_token}"},{"$set":{"processed_at":f"{datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}"}})
        return True
    else:
        return False

def changePass(access_token, password):
    access_token_db = client.access_token_db
    access_token_db_collection = access_token_db.access_token_db_collection
    entry = access_token_db_collection.find_one({"access_token": f"{access_token}"})
    user_creds = client.user_creds
    user_creds_collection = user_creds.user_creds_collection
    user_creds_collection.update_one({"name":f"{entry['db_name']}"},{"$set":{"password":f"{password}"}})

def showNotif(access_token):
    access_token_db = client.access_token_db
    access_token_db_collection = access_token_db.access_token_db_collection
    entry = access_token_db_collection.find_one({"access_token": f"{access_token}"})
    db_name = entry["db_name"]
    notif_db = entry["notif_collection"]
    db = client[db_name]
    data = db.get_collection(notif_db).find({},{"_id" : 0}).sort('_id', pymongo.DESCENDING).limit(10)
    return data

def showConfig(access_token):
    access_token_db = client.access_token_db
    access_token_db_collection = access_token_db.access_token_db_collection
    entry = access_token_db_collection.find_one({"access_token": f"{access_token}"})
    db_name = entry["db_name"]
    notif_db = entry["config_collection"]
    db = client[db_name]
    data = db.get_collection(notif_db).find({},{"_id" : 0}).sort('_id', pymongo.DESCENDING).limit(1)
    return data