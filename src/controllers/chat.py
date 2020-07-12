from src.app import app
from flask import json
from pymongo import MongoClient
from src.config import DB_URL, DB_NAME
from flask import request
import re
from src.helpers.errorHelpers import errorHelper, APIError, checkValidParams # Error404,
from src.helpers.apiResponse import data


dbChat = MongoClient(DB_URL).get_database(DB_NAME).chats
dbUser = MongoClient(DB_URL).get_database(DB_NAME).users
print(f"connected to db {DB_URL}")
# messages = client.get_default_database()["messages"]

User_id = []
@app.route("/chat/create/<name>")
def get_chat(name):
    #print("Request to create conversation with user_id: ")
    chatId = dbChat.find({"room": name}) #"messages": initMessages})
    return {"conversation_id": str(chatId)}

@app.route("/chat/create/<name>", methods=['POST'])
def create_chat(name):
    print("Request to create conversation with name: " + name)
    # if (validateUsername(username) == False):
    print(request.json)
    usersReq = request.json["users"]
    usersArray = []
    for user in usersReq: 
        print(user)
        user = dbUser.find_one({"user_name": {"$eq":user['name']}})
        usersArray.append(user)
    #initMessages = request.json["messages"]
    chatId = dbChat.insert({"room": name,"users":usersArray}) #"messages": initMessages})
    print(usersArray)
    return {"conversation_id": str(chatId)}

@app.route("/chat/<room>/adduser",  methods=['POST'])
def add_user(room):
    print("Request for update or add users in room", room)
    usersReq = request.json["users"]
    usersArray = []
    for user in usersReq: 
        print(user)
        user = dbUser.find_one({"user_name": {"$eq":user['name']}})
        if user != None:
            usersArray.append(user)

    users = dbChat.find_one({"room": {"$eq":room}})['users']
    users += usersArray
    #print(users)
    chatId = dbChat.update_one({"room": {"$eq":room}}, {'$set':{"users": users}})
    return {"conversation_id": str(chatId)}


@app.route("/chat/<room>/addmessage", methods=['POST'])
def add_message(room):
    print("To add a message to a user in room", room)
    
    messagesReq = request.json["message"]
    messageArray = []
    
    for message in messagesReq:
        print(message)
        if validateUserinRoom(message["name"]) == False:     
            messageArray.append(message)

    #messages = dbChat.find_one({"room": {"$eq":room}}) #['messages']
    #messages += messageArray
    print(messageArray)
    #chatId = dbChat.update_one({"room": {"$eq":room}}, {'$set':{"messages": messageArray}})
    return {"messages": messageArray}
"""
chatId = dbChat.insert({"room": room, "user": username, "message": message})
        return {"message":str()}
        #params: converstation_id, user_id, text
        #raise exception if user not part of this conversation
        return #message_id

"""
def validateUserinRoom(username):
    print("validateUserinRoom==", username)
    if dbChat.find({"users.user_name":{"$eq":username}}).limit(1).count() == 0:
        raise Exception ("This user is not in this room, try with another")
    return False









"""
@app.route("/chat/<conversation_id>/list", methods=['POST']) 
def converstationParams(conversation_id):

    return #json with all messages from this "conversation_id"
"""