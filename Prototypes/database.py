from dotenv import load_dotenv, find_dotenv
import os, pprint
from pymongo import MongoClient
from datetime import datetime, timedelta

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://Group1:{password}@testdb.dhmeogy.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)

# dbs = client.list_database_names()
# test_db = client.test
# collections = test_db.list_collection_names()

# # def insert_test_doc():
# collection = test_db.test
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwMTk2OTAwMCwianRpIjoiNzk3MWRlMjQtNmVmMy00OGM5LWI1ZmQtYjljNmEzMjkwY2JlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Im1hbmpyZWthcnN1ZGVzaDE1QGdtYWlsLmNvbSIsIm5iZiI6MTcwMTk2OTAwMCwiZXhwIjoxNzAxOTY5OTAwfQ.u7_mirRBrRZbrwvQq5czZVlcjr4-efwcG-M8MoigwwE"

access_token_db = client.access_token_db
access_token_db_collection = access_token_db.access_token_db_collection
entry = access_token_db_collection.find_one({"access_token": f"{access_token}"})
db_name = entry["db_name"]
db_collection = entry["analysis_collection"]
db = client[db_name]

test_document = {
    # "Averages" : [30.13517241, 29.29034483, 29.64896552, 29.73103448, 30.50068966, 29.20068966, 29.46413793],
    # "Start" : datetime.strptime('04/12/2023','%d/%m/%Y'),
    # "End" : datetime.strptime('04/12/2023','%d/%m/%Y') + timedelta(days=6),
    # "Linear_Regression" : [29.901674876847284, 29.85379310344827, 29.805911330049256, 29.758029556650243, 29.710147783251227, 29.662266009852214, 29.614384236453198]
    "Averages" : [30.13517241,29.29034483,29.64896552,29.73103448,30.50068966,29.20068966,29.46413793,30.12965517,29.29034483,29.64896552,29.73055556,30.49862069,29.20689655,29.47103448,30.13517241,29.29586207,29.64896552,29.73793103,30.50068966,29.20068966,29.46758621,29.46896552,30.11310345,29.29655172,29.64896552,29.73655172,30.50068966,29.20068966,29.50827586,30.15310345],
    "Start" : datetime.strptime('01/12/2023','%d/%m/%Y'),
    "End" : datetime.strptime('01/12/2023','%d/%m/%Y') + timedelta(days=30),
    "Linear_Regression" : [29.718025455264367, 29.718068760107528, 29.718112064950684, 29.718155369793845, 29.718198674637005, 29.71824197948016, 29.718285284323322, 29.718328589166482, 29.71837189400964, 29.7184151988528, 29.71845850369596, 29.718501808539116, 29.718545113382277, 29.718588418225437, 29.718631723068594, 29.718675027911754, 29.718718332754914, 29.71876163759807, 29.71880494244123, 29.71884824728439, 29.71889155212755, 29.71893485697071, 29.71897816181387, 29.719021466657026, 29.719064771500186, 29.719108076343346, 29.719151381186503, 29.719194686029663, 29.719237990872823, 29.71928129571598]

}
inserted_id = db.get_collection(db_collection).insert_one(test_document).inserted_id
print(inserted_id)

# # insert_test_doc()
# production = client.production
# person_collection = production.person_collection

# def create_documents():
#     first_names = ["A", "B", "C", "D", "E"]
#     last_names = ["a", "b", "c", "d", "e"]
#     ages = [21, 45, 12, 54, 23]

#     docs = []

#     for first_name, last_name, age in zip(first_names, last_names, ages):
#         doc = {"first_name": first_name, "last_name": last_name, "age": age}
#         docs.append(doc)
#     person_collection.insert_many(docs)

# printer = pprint.PrettyPrinter()

# def find_all_people():
#     people = person_collection.find()
    
#     for person in people:
#         printer.pprint(person["first_name"])

# find_all_people()

# def find_A():
#     A = person_collection.find_one({"first_name": "A"})
#     printer.pprint(A["last_name"])

# # find_A()
