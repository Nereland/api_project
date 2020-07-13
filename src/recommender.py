from src.app import app
from flask import json
from pymongo import MongoClient
from src.config import DB_URL
from flask import request
import re
from src.helpers.apiResponse import data

client = MongoClient(DB_URL)
print(f"connected to db {DB_URL}")


@app.route("/user/<user_id>/recommend`", methods=['GET'])
def recomendations():
    return #json array with 3 top similar users

