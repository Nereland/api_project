from pymongo import MongoClient
from src.config import DB_URL
from src.config import DB_URL, DB_NAME


dbChat = MongoClient(DB_URL).get_database(DB_NAME).chats
dbClient = MongoClient(DB_URL).get_database('sentimentApi')
print(f"connected to validations db {DB_URL}")

#Function to validate wheter a username already exists in the users collection
def validateUsername(username):
    print ("validateUsername == ", username)
    return (False, True) [dbClient.users.find({"user_name":{"$eq":username}}).limit(1).count() > 0]


#Function to validate if a user exists in one room    
def validateUserinRoom(username):
    print("validateUserinRoom==", username)
    return (False, True) [dbChat.find({"users.user_name":{"$eq":username}}).limit(1).count() == 0]
       


# Function to validate if a room already exists
def validateRoom(name):
    print("validateRoom==", name)
    return (False, True)[dbChat.find({"room":{"$eq":name}}).limit(1).count() > 0]
       
