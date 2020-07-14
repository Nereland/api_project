# Sentiment recognizer API

Animated films are usally considered a "children thing"... 
![MONONOKE](/assets/MONONOKE.jpg)
but we all know is not such, don't we? 

![ghost](/assets/ghost.jpg)

However, even when we talk about animated films for children, there are all types of feelings that it's worth to realize. They help children(and adults) to understand grief, happinesss, fear, sadness..

![MONONOKE2](/assets/MONONOKE2.jpeg)

I created an API to recognize feelings, and for this I chose a small piece of a very well known children film... 
![all](/assets/all.jpg)
I have no doubt all of you can recognize this image, and, if you have seen the film, you will also recognize that you were not neutral to Simba's adventures... some of them amazing, some of them scary, others really sad... 


# Creating and running the SentimentApi

By using [Flask](https://flask.palletsprojects.com/en/1.1.x/) I created this API to store the characters (users), the conversations (chats) and the dialogues (messages) into [MongoDB](https://www.mongodb.com/). The conexion between MongoDB and the SentimentApi was conducted with [PyMongo](https://pymongo.readthedocs.io/en/stable/). If you wish, you can read about them by clicking on the names in blue.


### Inserting main characters

First of all, With "POST" method, I created users, for the sake of simplicity, I  chose just of them 
![CHARACTERS](/assets/CHARACTERS.png)

By doing defensive programming, I made sure each character was inserted only once in the database, in case it was already there, an infomative messages would come up.

### Chats/conversations 

Then, also using "POST", I created four chats:
**Birth**,
![scar](/assets/scar.jpg)

 **Growing up, Elephant Graveyard and Hakuna Matata** 


![growing_up](/assets/growing_up.png)

### Messages/Dialogues

I also made sure that chats could not be reapeated, after that, and also with post method, I inserted the dialogues/messages into the MongoDB. In this case I let the program accept new messages given that it should work like a chat room does (for further information the instructions file is also available in this repo).

Finally with GET method the SentimentApi would return a [json](https://www.json.org/json-es.html) array with all the messages from a given chat. This last step was important to run the sentiment analysis as I will explain below

## SENTIMENT ANALYSIS WITH NLTK

![Captura de pantalla 2020-07-14 a las 19.31.30](/assets/Captura%20de%20pantalla%202020-07-14%20a%20las%2019.31.30.png)


We were suggested to use Natural Language Toolkit [NLTK](https://www.nltk.org/) to conduct the analysis. 
This was an extremely usefull tool to analyse the general feeling of every chat as it would get a json and read it... as simple as that. 

**And just to conclude, I would like to point out some findings...**

When I analysed the **Birth** chat... the general sentiments were 'mostly unhappy: negative polarity', 'negative:', 0.053, 'positive', 0.025 (I must confess most of the dialogues here belong to the conversation between Scar and Mufasa, so, not really surprising)

The **Growing up** chat in which Mufasa talks to Simba to show him the limits of their territory has a positive polarity : 'mostly happy: positive plolarity', 0.031, 0.069


When I analysed the **Elephant Graveyard** chat... the general sentiments were also "mostly unhappy: negative polarity', 'negative:', 0.069, 'positive', 0.035, but this is not suprising... is it?
           ![elephant_graveyard](/assets/elephant_graveyard.jpeg)


And... what do you think about **Hakuna Matata** room?? As you may have thought, the polarity is mainly positive (0.093)



