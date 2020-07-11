from pymongo import MongoClient
from src.config import DB_URL

dbClient = MongoClient(DB_URL).get_database('sentimentApi')
print(f"connected to db {DB_URL}")

def validateUsername(username):
    print ("validateUsername == ", username)
    return (False, True) [dbClient.users.find({"user_name":{"$eq":username}}).limit(1).count() > 0]