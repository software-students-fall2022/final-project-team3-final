from pymongo import MongoClient

# provide MongoDB Atlas URL
CONNECTION_STRING = "mongodb+srv://user:<root>@cluster0.fgszvaj.mongodb.net/?retryWrites=true&w=majority"
# create connection
client = MongoClient(CONNECTION_STRING)
# find database and collection
database = client["recipes"]
collection = database["Data"]
