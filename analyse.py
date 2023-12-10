import time, os
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
from datetime import datetime, date, timedelta
from Analytics.Vedantrik.Linear_Regression.linear_regression import linear_regression

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")
connection_string = f"mongodb+srv://Group1:{password}@testdb.dhmeogy.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)

done = False

today = date.today().strftime('%d')
print("Program started at:",today)

target = (date.today() + timedelta(days=7)).strftime('%d')
print("Starting process at:",target)

def add_points():
    # get the creds from .env

    # get the names of databasess to update

    # open that db

    # read db get points

    # calculate avg

    # 7 points for each day
    # points = [30.13517241379305, 29.29034482758627, 29.64896551724133, 29.73103448275868, 30.50068965517238, 29.2006896551724, 29.46413793103448]
    points = [30.13517241,29.29034483,29.64896552,29.73103448,30.50068966,29.20068966,29.46413793,30.12965517,29.29034483,29.64896552,29.73055556,30.49862069,29.20689655,29.47103448,30.13517241,29.29586207,29.64896552,29.73793103,30.50068966,29.20068966,29.46758621,29.46896552,30.11310345,29.29655172,29.64896552,29.73655172,30.50068966,29.20068966,29.50827586,30.15310345]

    # get the slope and y-int
    print(linear_regression(points))

    # add to db -> 7 points, slope, y-int,

    # done = True

    # target = today, target = now + 7
    pass

if (today>=target):
    print("Its due")
    add_points()
else:
    print("Yet to due")

add_points()