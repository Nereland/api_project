from src.app import app
from flask import json
from pymongo import MongoClient
from src.config import DB_URL, DB_NAME
from flask import request
from src.helpers.errorHelpers import errorHelper, APIError, checkValidParams # Error404,
from src.helpers.apiResponse import data
from src.helpers.apiValidations import validateUserinRoom, validateRoom


dbChat = MongoClient(DB_URL).get_database(DB_NAME).chats
dbUser = MongoClient(DB_URL).get_database(DB_NAME).users
print(f"connected to chat db {DB_URL}")
# messages = client.get_default_database()["messages"]


# 1.- Add a new chat/conversation with an array of users to the chat collection 

@app.route("/chat/create/<name>", methods=['POST'])
def create_chat(name):
    print("Request to create conversation with name: " + name)
    if validateRoom(name) == False:
        print(request.json)
        usersReq = request.json["users"]
        usersArray = []
        for user in usersReq: 
            print(user)
            user = dbUser.find_one({"user_name": {"$eq":user['name']}})
            usersArray.append(user)
        chatId = dbChat.insert({"room": name,"users":usersArray})
        print(usersArray)
        return {"conversation_id": str(chatId)}
    else:
       return {"message":"This room already exists, you cannot create two rooms with the same name"}



# 2.- Add a new user to a chat room

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

# 3.- Add messages for each user in each  conversation

@app.route("/chat/<room>/addmessages", methods=['POST'])
def add_message(room):
    print("To add a message to a user in room", room)
    
    messagesReq = request.json["message"]
    messageArray = []
    
    for message in messagesReq:
        #print(message)
        if validateUserinRoom(message["name"]) == False:     
            messageArray.append(message)
        else: 
            print("User doesnt belong to this room")
       
    messagesDb = dbChat.find_one({"room": {"$eq":room}},{"messages":1})
    print(messagesDb)
    if ("messages" in messagesDb):
        messages = messagesDb["messages"] + messageArray
    else:
        messages = messageArray
        #print(messageArray)
    chatId = dbChat.update_one({"room": {"$eq":room}}, {'$set':{"messages": messages}})
    return {"message": messageArray}
        

# 4.- Get an array of messages from a conversation

@app.route("/chat/<room>")
def get_chat(room):
    print("Request to get messages from a conversation")
    messagesDb = dbChat.find_one({"room": {"$eq":room}}, {"messages.message":1})
    if ("messages" in messagesDb):
        messages = messagesDb["messages"]
    else:
        messages = []
        
    print(messages)
    return {"messages":messages}


