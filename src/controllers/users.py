from src.app import app
from flask import json
from pymongo import MongoClient
from src.config import DB_URL, DB_NAME
from flask import request
from src.helpers.apiResponse import data
from src.helpers.apiValidations import validateUsername

dbUser = MongoClient(DB_URL).get_database(DB_NAME).users
print(f"connected to db {DB_URL}")
# messages = client.get_default_database()["messages"]

@app.route("/user/create/<username>", methods=['POST'])
def create_user(username): 
    print("Request to create user with username: ", username)
    if validateUsername(username) == False:
        user = dbUser.insert({"user_name": username})
        res = {"user_id": str(user)}
    else:
        user = dbUser.find_one({"user_name": {"$eq":username}},{"username":0})["_id"]
        res = {"message": "User already exists", "user_id" : str(user)}
                              
    return res

