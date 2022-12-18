from flask import Flask, render_template, request, redirect, abort, url_for, make_response, flash
from pymongo import MongoClient
from dotenv import dotenv_values
import os

# global variables
config = dotenv_values(".env")
app = Flask(__name__)

# connect to the database
# provide MongoDB Atlas URL
CONNECTION_STRING = "mongodb+srv://user:<root>@cluster0.fgszvaj.mongodb.net/?retryWrites=true&w=majority"
# create connection
client = MongoClient(CONNECTION_STRING)
try:
    # verify the connection works by pinging the database
    # The ping command is cheap and does not require auth.
    client.admin.command('ping')
    # database = cxn['___'] # store a reference to the database
    # if we get here, the connection worked!
    database = client["recipes"]
    collection = database["Data"]
    print(' *', 'Connected to MongoDB!')
except:
    print("MongoDB not connected.")


@app.route("/")
def index():
    return render_template('index.html')


# run the app
if __name__ == "__main__":
    app.run()
