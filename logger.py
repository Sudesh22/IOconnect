from dotenv import load_dotenv, find_dotenv
import os, pprint, pymongo
from pymongo import MongoClient
from datetime import datetime,timedelta
from verification import send_mail
from authenticate import getUser

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://Group1:{password}@testdb.dhmeogy.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)

def log_alert(condition, Device_Id=None, access_token=None):
    devices_db = client.devices_db
    devices_db_collection = devices_db.devices_db_collection
    entry = devices_db_collection.find_one({"device_id": Device_Id})
    print(entry)
    db_name = str(entry["username"])
    db_collection = db_name+"@notif"
    db = client[db_name]
    now = datetime.now().strftime("%d/%m/%y %H:%M:%S")
    if condition == "alert":
        data = {
            "company"     : entry['company_name'],
            "device_id"   : Device_Id,
            "description" : "The box was tampered with",
            "headline"    : "Box Tampered!!!",
            "read"        : False,
            "timestamp"   : now,
            "condition"   : "alert",
    }
    elif condition == "promotion":
        data = {
        "company"     : entry["company_name"],
        "device_id"   : Device_Id,
        "description" : "Team IOconnect wishes you a very Happy New Year",
        "headline"    : "Another year of Togetherness!",
        "read"        : False,
        "timestamp"   : "01/01/24 00:00:00",
        "condition"   : "promotion",
    }
    elif condition == "signIn":
        data = {
        "company"     : entry["company_name"],
        "device_id"   : Device_Id,
        "description" : "A new device just signed in!",
        "headline"    : "Security Alert",
        "read"        : False,
        "timestamp"   : now,
        "condition"   : "signIn",
    }
    elif condition == "action":
        data = {
        "company"     : entry["company_name"],
        "device_id"   : Device_Id,
        "description" : "The heater was turned off!",
        "headline"    : "Action Performed",
        "read"        : False,
        "timestamp"   : now,
        "condition"   : "action",
    }
    db.get_collection(db_collection).insert_one(data).inserted_id
    return ("Data inserted with id:")

def log_to_database(data, Json):
    devices_db = client.devices_db
    devices_db_collection = devices_db.devices_db_collection
    entry = devices_db_collection.find_one()
    print(entry)
    db_name = str(entry["username"])
    db_collection = db_name+"@dash"
    db = client[db_name]
    db.get_collection(db_collection).insert_one(data).inserted_id
    return ("Data inserted with id:")

def add_user(data,access_token):
    user_creds = client.user_creds
    user_creds_collection = user_creds.user_creds_collection
    
    db_name = str(data["name"])+"@dash"
    db_config = str(data["name"])+"@config"
    db_notif = str(data["name"])+"@notif"
    db_predict = str(data["name"])+"@predict"
    db_analysis = str(data["name"])+"@analysis"
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
    db.create_collection(db_analysis)
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

def showHome(access_token):
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

def showAnalysis(access_token,time_frame):
    access_token_db = client.access_token_db
    access_token_db_collection = access_token_db.access_token_db_collection
    entry = access_token_db_collection.find_one({"access_token": f"{access_token}"})
    db_name = entry["db_name"]
    db_collection = entry["analysis_collection"]
    db = client[db_name]
    date = (datetime.now()-timedelta(days = int((datetime.now().strftime("%u")))-1))
    print(date)
    if time_frame == "Weekly":
        data = db.get_collection(db_collection).find({"Start":str(date).split()[0],"End": str(date + timedelta(days=6)).split()[0]},{"_id" : 0,"Start":0,"End":0,"Averages1":0,"Averages2":0})
    elif time_frame == "Monthly":
        data = db.get_collection(db_collection).find({"Start":str(date).split()[0],"End": str(date + timedelta(days=30)).split()[0]},{"_id" : 0,"Start":0,"End":0,"Averages":0})
    elif time_frame == "Yearly":
        data = db.get_collection(db_collection).find({"Start":str(date).split()[0],"End": str(date + timedelta(days=30)).split()[0]},{"_id" : 0,"Start":0,"End":0,"Averages":0})
    # print(type(data))
    # print(time_frame)
    DataList = []
    for d in data:
        DataList.append(tuple(d.values()))
        # print(tuple(d))
    # print(DataList[0])    
    return DataList[0]

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
    entry = change_pass_db_collection.find({"access_token": f"{access_token}"},).sort('_id', pymongo.DESCENDING).limit(1)[0]
    print(entry["expires_at"])
    print(datetime.now())
    print(entry["expires_at"] > datetime.now())
    if entry["expires_at"] > datetime.now():
        change_pass_db_collection.update_one({"access_token": access_token, "expires_at": entry["expires_at"]},{"$set":{"processed_at":f"{datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}"}})
        return True
    else:
        return False

def changePass(access_token, password):
    access_token_db = client.access_token_db
    access_token_db_collection = access_token_db.access_token_db_collection
    entry = access_token_db_collection.find({"access_token": f"{access_token}"},).sort('_id', pymongo.DESCENDING).limit(1)[0]
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
    data = db.get_collection(notif_db).find({},{"_id" : 0,"company":0,"device_id":0})
    DataList = []
    for d in data:
        DataList.append(tuple(d.values()))
        # print(tuple(d))
    print(DataList)
    return DataList

def showConfig(access_token):
    access_token_db = client.access_token_db
    access_token_db_collection = access_token_db.access_token_db_collection
    entry = access_token_db_collection.find_one({"access_token": f"{access_token}"})
    db_name = entry["db_name"]
    config_db = entry["config_collection"]
    db = client[db_name]
    data = db.get_collection(config_db).find({},{"_id" : 0}).sort('_id', pymongo.DESCENDING).limit(1)
    return data

def addConfig(access_token, configMail):
    access_token_db = client.access_token_db
    access_token_db_collection = access_token_db.access_token_db_collection
    entry = access_token_db_collection.find_one({"access_token": f"{access_token}"})
    db_name = entry["db_name"]
    config_db = entry["config_collection"]
    db = client[db_name]
    now = datetime.strptime(datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),"%d/%m/%Y, %H:%M:%S")
    data = {"configMail" :           configMail,
            "access_token":          access_token,
            "date_added":            now,
           } 
    db.get_collection(config_db).insert_one(data)
    return {"Status": "recovery mail added successfully"}

def dev_db():
    devices_db = client.devices_db
    devices_db_collection = devices_db.devices_db_collection
    data = {"device_id"          :    1 ,
            "microcontroller"    :    "STM32",
            "sensors_used"       :    {"temp" : "PT100"},
            "username"           :    "SUDESH",
            "company_name"       :    "Vedantrik",
           } 
    inserted_id = devices_db_collection.insert_one(data).inserted_id