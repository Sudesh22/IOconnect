from dotenv import load_dotenv, find_dotenv
import os, pprint
from pymongo import MongoClient

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://Group1:{password}@testdb.dhmeogy.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)

dbs = client.list_database_names()
test_db = client.test
collections = test_db.list_collection_names()

def insert_test_doc():
    collection = test_db.test
    test_document = {
        "name" : "Sudesh",
        "type" : "Test"
    }
    inserted_id = collection.insert_one(test_document).inserted_id
    print(inserted_id)

# insert_test_doc()
production = client.production
person_collection = production.person_collection

def create_documents():
    first_names = ["A", "B", "C", "D", "E"]
    last_names = ["a", "b", "c", "d", "e"]
    ages = [21, 45, 12, 54, 23]

    docs = []

    for first_name, last_name, age in zip(first_names, last_names, ages):
        doc = {"first_name": first_name, "last_name": last_name, "age": age}
        docs.append(doc)
    person_collection.insert_many(docs)

create_documents()
