from dotenv import load_dotenv, find_dotenv
import os, pprint, sqlite3
from pymongo import MongoClient
import pymongo

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://Group1:{password}@testdb.dhmeogy.mongodb.net/"

client = MongoClient(connection_string)
def log_to_database(data):
    SUDESH = client.SUDESH
    coll_name = SUDESH.get_collection("SUDESH@manjrekarsudesh15@gmail.com")

    inserted_id = coll_name.insert_one(data).inserted_id
    return ("Data inserted with id:", inserted_id)

conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute("SELECT * FROM DataLogging ORDER BY rowid DESC LIMIT 5 ")
items = c.fetchall()
# print(items[1][1])
for item in items:
    # for i in enumerate(item, start=1):
        # print(item[1])
    print(item)
    data = {
            "Device_Id" : item[0],
            "Status"    : item[1],
            "Temp"      : item[2],
            "Humi"      : item[3],
            "Time"      : item[4],  }
    log_to_database(data)
print(data)

# db.collection.find().limit(1).sort({$natural:-1}) 
