# W6 Project - Chat Sentiment Analysis Service

**Description:** You want to analyze conversations form a chat messaging app (like slack or whatsapp). The purpose of the analysis is to extract
sentiment metrics people interactions. We are going to create an api service for this purpose. In our current case, the chat service will call our api
endpoints and it's our task to create those endpoints for:

- A) Store the data in a `mongodb` database
- B) Do the analysis of the data inside `mongodb`

You will practice in this project:

- Create an API using `flask`
- Use `pymongo` insert methods
- NLTK sentiment analysis
- Docker, Heroku and Cloud databases
- Recommender systems

## Project Goals

**Main goal**: Analyze the conversations coming from a chat like `slack`

- L1🧐- Write an API in `flask` just to store chat messages in a mongodb database.
- L2 (A)🥳- Extract sentiment from chat messages and perform a report over a whole conversation
- L2 (B)🤭- Recommend friends to a user based on the contents from chat `documents` using a recommender system with `NLP` analysis.
- L3😎- Deploy the service with docker to heroku and store messages in a cloud database.
- L4🔥- **HOT** Do it real, use slack API to get messages and analyze the messages of our `datamad` channel.
  - `https://api.slack.com/`

**IMPORTANT:** All api endpoints must return JSON messages

You have to create an api with all this endpoints:

### L1. User endpoints

- (GET) `/user/create/<username>`

  - **Purpose:** Create a user and save into DB
  - **Params:** `username` the user name
  - **Returns:** `user_id`

### L1. Chat endpoints

- (GET) `/chat/create`
  - **Purpose:** Create a conversation to load messages on it. You can use a `jupyter notebook` to test it using the requests module.
  - **Params:** An array of users ids `[user_id]`
  - **Returns:** `conversation_id`
- (GET) `/chat/<conversation_id>/adduser`
  - **Purpose:** Add a user to a chat conversation
  - **Params:** `user_id`
  - **Returns:** `conversation_id`
- (POST) `/chat/<conversation_id>/addmessage`
  - **Purpose:** Add a message to a conversation. Important: Before adding the chat message to the database, check that the incoming user is part of this conversation. If not, raise an exception.
  - **Params:**
    - `conversation_id`: Chat to store message
    - `user_id`: the user that writes the message
    - `text`: Message text
  - **Returns:** `message_id`
- (GET) `/chat/<conversation_id>/list`
  - **Purpose:** Get all messages from `conversation_id`
  - **Returns:** json array with all messages from this `conversation_id`

### L2. Sentiment analysis and recommender

- (GET) `/chat/<conversation_id>/sentiment`
  - **Purpose:** Analyze messages from `chat_id`. Use `NLTK` sentiment analysis package for this task
  - **Returns:** json with all sentiments from messages in the chat

- (GET) `/user/<user_id>/recommend`
  - **Purpose:** Recommend friend to this user based on chat contents
  - **Returns:** json array with top 3 similar users

## References and links

- [https://flask.palletsprojects.com/]
- [https://www.getpostman.com/]
- [https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.insert_one]
- [https://api.mongodb.com/python/current/tutorial.html]
- [https://mermaid-js.github.io/mermaid/#/entityRelationshipDiagram]

NLP & Text Sentiment Analysis:

- [https://www.nltk.org/]
- [https://towardsdatascience.com/basic-binary-sentiment-analysis-using-nltk-c94ba17ae386]
- [https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk]

Heroku & Docker

- [<https://docs.docker.com/engine/reference/builder/]>
- [<https://runnable.com/docker/python/dockerize-your-python-application]>
- [<https://devcenter.heroku.com/articles/container-registry-and-runtime]>
- [<https://devcenter.heroku.com/categories/deploying-with-docker]>

Mongodb Atlas

- [<https://www.mongodb.com/cloud/atlas]>

[![](https://mermaid.ink/img/eyJjb2RlIjoiY2xhc3NEaWFncmFtXG4gICAgICBDaGF0SXRlbSA8fC0tIENvbnZlcnNhdGlvbiA6IFwiY29udGFpbnNcIlxuICAgICAgQ2hhdEl0ZW0gPHwtLSBVc2VyIDogXCJoYXMgc2VudFwiXG4gICAgICBDb252ZXJzYXRpb24gPHwtLSBVc2VyIDogXCJpcyBwYXJ0IG9mXCJcbiAgICAgIGNsYXNzIENoYXRJdGVte1xuICAgICAgICAgICtPYmplY3RJZCBcIl9pZFwiXG4gICAgICAgICAgK1N0cmluZyBtZXNzYWdlX3RleHRcbiAgICAgICAgICArT2JqZWN0SWQgdXNlclxuICAgICAgICAgICtPYmplY3RJZCBjb252ZXJzYXRpb25cbiAgICAgIH1cbiAgICAgIGNsYXNzIENvbnZlcnNhdGlvbntcbiAgICAgICAgICArT2JqZWN0SWQgXCJfaWRcIlxuICAgICAgICAgICtTdHJpbmcgbmFtZVxuICAgICAgICAgICtBcnJheTxPYmplY3RJZD4gdXNlcnNcbiAgICAgIH1cbiAgICAgIGNsYXNzIFVzZXJ7XG4gICAgICAgICAgK09iamVjdElkIFwiX2lkXCJcbiAgICAgICAgICArU3RyaW5nIG5hbWVcbiAgICAgIH1cbiIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiY2xhc3NEaWFncmFtXG4gICAgICBDaGF0SXRlbSA8fC0tIENvbnZlcnNhdGlvbiA6IFwiY29udGFpbnNcIlxuICAgICAgQ2hhdEl0ZW0gPHwtLSBVc2VyIDogXCJoYXMgc2VudFwiXG4gICAgICBDb252ZXJzYXRpb24gPHwtLSBVc2VyIDogXCJpcyBwYXJ0IG9mXCJcbiAgICAgIGNsYXNzIENoYXRJdGVte1xuICAgICAgICAgICtPYmplY3RJZCBcIl9pZFwiXG4gICAgICAgICAgK1N0cmluZyBtZXNzYWdlX3RleHRcbiAgICAgICAgICArT2JqZWN0SWQgdXNlclxuICAgICAgICAgICtPYmplY3RJZCBjb252ZXJzYXRpb25cbiAgICAgIH1cbiAgICAgIGNsYXNzIENvbnZlcnNhdGlvbntcbiAgICAgICAgICArT2JqZWN0SWQgXCJfaWRcIlxuICAgICAgICAgICtTdHJpbmcgbmFtZVxuICAgICAgICAgICtBcnJheTxPYmplY3RJZD4gdXNlcnNcbiAgICAgIH1cbiAgICAgIGNsYXNzIFVzZXJ7XG4gICAgICAgICAgK09iamVjdElkIFwiX2lkXCJcbiAgICAgICAgICArU3RyaW5nIG5hbWVcbiAgICAgIH1cbiIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)
