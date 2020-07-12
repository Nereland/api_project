
client = MongoClient(DB_URL)
print(f"connected to db {DB_URL}")
# messages = client.get_default_database()["messages"]

def messageCollectionExists():
    # return (True, False)[client.messages.find({'messages'}).count() > 0]
    return (True, False)["messages" in client.collection_names()]

@app.route('/greet', methods=['GET'])
def greetParams():
    greetName = "A " + request.args.get("name") 
    intensity = request.args.get("intensity")
    print(f"Requesting greet for {greetName}")
    return {'Saludo': greetName + " " +intensity}

@app.route('/greet/<name>', methods=['GET','POST'])
def greet(name):
    print("Requesting to === " +request.method)
    dbExist = messageCollectionExists()
    print("Database collection exits? ", dbExist)
    if (request.method == "GET"):
        print(f"Requesting GET greet for {name}")
        intensity = request.args.get("intensity")
        greetName = f"A {name}, {intensity} "
        return {'Saludo': greetName }
    elif (request.method == "POST"):
        print(f"Requesting CREATE greet for {name}")
        intensity = request.args.get("intensity")
        greetName = f"A {name}, {intensity} "
        return {'Saludo': greetName }
