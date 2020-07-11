from src.app import app
from flask import json
from pymongo import MongoClient
from src.config import DB_URL
from flask import request
import re
from src.helpers.errorHelpers import errorHelper, APIError, checkValidParams # Error404,
from src.helpers.apiResponse import data


chatColl = MongoClient(DB_URL).get_database('sentimentApi').chats
print(f"connected to db {DB_URL}")
# messages = client.get_default_database()["messages"]

User_id = []
@app.route("/chat/create/<name>", methods=['POST'])
def chat_create(name):
    #print("Request to create conversation with user_id: ")
    # if (validateUsername(username) == False):
    userArray = request.json["users"]
    initMessages = request.json["messages"]
    chatId = chatColl.insert({"room": name,"users":userArray, "messages": initMessages})
    print(userArray)
    return {"conversation_id": str(chatId)}

@app.route("/chat/<conversation_id>/adduser", methods=['POST'])
def add_user(conversation_id):
    #user_id es el param
    return #conversatioin id

@app.route("/chat/<conversation_id>/addmessage", methods=['POST'])
def add_message():
    #params: converstation_id, user_id, text
    #raise exception if user not part of this conversation
    return #message_id

@app.route("/chat/<conversation_id>/list", methods=['POST']) 
def converstationParams(conversation_id):

    return #json with all messages from this "conversation_id"