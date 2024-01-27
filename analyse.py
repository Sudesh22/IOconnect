import time, os, pymongo
import numpy as np
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
from datetime import datetime, date, timedelta
from Analytics.Vedantrik.Linear_Regression.linear_regression import linear_regression

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")
connection_string = f"mongodb+srv://Group1:{password}@testdb.dhmeogy.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)

today = date.today().strftime('%Y-%m-%d')
print("Program started at:",today)

target = (date.today() + timedelta(days=6)).strftime('%Y-%m-%d')
print("Starting process at:",target)

devices_db = client.devices_db
devices_db_collection = devices_db.devices_db_collection
entry = devices_db_collection.find_one()
print(entry)
db_name = str(entry["username"])
db = client[db_name]
dash_collection = db_name+"@dash"
anlys_collection = db_name+"@analysis"

def add_to_db(p1,p2,l1,l2):
    test_document = {
    "Averages1" : p1.tolist(),
    "Averages2" : p2.tolist(),
    "Start" : today,
    "End" : target,
    "Linear_Regression1" : l1,
    "Linear_Regression2" : l2,
    }

    inserted_id = db.get_collection(anlys_collection).insert_one(test_document)
    print("Data added to Db")

def eval_points():
    # get the names of databases to update    
    
    # read db get points
    points1 = np.array([])
    points2 = np.array([])
    for i in range(7):
        tgt = (date.today() + timedelta(days=i)).strftime('%Y-%m-%d')
        data = db.get_collection(dash_collection).find({"Date":tgt},{"_id" : 0}).sort('_id', pymongo.DESCENDING)
        DataList1 = np.array([])
        DataList2 = np.array([])
        for d in data:
            DataList1 = np.append(DataList1,tuple(d.values())[1])
            DataList2 = np.append(DataList2,tuple(d.values())[2])
    
        # calculate avg
        points1 = np.append(points1,np.mean(DataList1))
        points2 = np.append(points2,np.mean(DataList2))
        print("Data average for date:", tgt, "is t1:", points1[i], " t2:", points2[i])

    # get the linear regression points
    lg1 = list(linear_regression(points1)['points'].values())
    lg2 = list(linear_regression(points2)['points'].values())

    # add to db -> 7 points per sensor, linregress points for 2 sensors
    add_to_db(points1,points2,lg1,lg2)

    # target = today, target = now + 6
    today = target
    target = (datetime.strptime(target,'%Y-%m-%d') + timedelta(days=6)).strftime('%Y-%m-%d')

if (today>=target):
    print("Its due")
    add_points()
else:
    print("Yet to due")