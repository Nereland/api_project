
from src.app import app
from flask import json
from pymongo import MongoClient
from src.config import DB_URL
from flask import request
import re
from src.helpers.errorHelpers import errorHelper, APIError, checkValidParams # Error404,
from src.helpers.apiResponse import data

client = MongoClient(DB_URL)
print(f"connected to db {DB_URL}")


@app.route('/chat/<conversation_id>/sentiment', methods=['GET'])
def sentiment():
    #analyze each message from chat_id
    #use NTKL
    return #json with all sentiments from messages in the chat

