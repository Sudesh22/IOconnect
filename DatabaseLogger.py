from dotenv import load_dotenv, find_dotenv
import os, pprint, sqlite3
from pymongo import MongoClient
import pymongo

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://Group1:{password}@testdb.dhmeogy.mongodb.net/"

client = MongoClient(connection_string)
# def log_to_database(data):
#     sensor_db = client.sensorDb
#     sensor_db_collection = sensor_db.sensor_db_collection
#     inserted_id = sensor_db_collection.insert_one(data).inserted_id
#     return ("Data inserted with id:", inserted_id)

# conn = sqlite3.connect('test.db')
# c = conn.cursor()
# c.execute("SELECT * FROM DataLogging ORDER BY rowid DESC LIMIT 5 ")
# items = c.fetchall()
# # print(items[1][1])
# for item in items:
#     # for i in enumerate(item, start=1):
#         # print(item[1])
#     print(item)
#     data = {
#             "Device_Id" : item[0],
#             "Status"    : item[1],
#             "Temp"      : item[2],
#             "Humi"      : item[3],
#             "Time"      : item[4],  }
#     log_to_database(data)
# print(data)

# db.collection.find().limit(1).sort({$natural:-1}) 
def showData():
    sensor_db = client.sensorDb
    sensor_db_collection = sensor_db.sensor_db_collection
    data = sensor_db_collection.find({},{"_id" : 0}).sort('_id', pymongo.DESCENDING).limit(7)
    # print(type(data))
    DataList = []
    for d in data:
        DataList.append(tuple(d.values()))
        # print(tuple(d))

    # print(type(DataList))
    return DataList