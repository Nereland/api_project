#Function to study my script structure 

def messages(x):
    converList = []
    for i in range(len(x)):
        message = {"name": x[i]["user"],
                   "message": x[i]["message"],
                  "room":x[i]["conversation"]}
        converList.append(message)
    return converList



def players(x):
    namelist= []
    for user in x:
        name = {"name": user}        
        namelist.append(name)
    return namelist



def conversation(x):
    conversatlist = []
    for chat in range(len(x)):
        conversation = {"name": x[chat]["user"],
                   "conversation": x[chat]["conversation"]}
        if conversation not in conversatlist:
            conversatlist.append(conversation)
    return conversatlist
