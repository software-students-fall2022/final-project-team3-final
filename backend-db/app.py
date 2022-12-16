from pymongo import MongoClient
from flask import Flask
from flask import request
from flask import render_template

app= Flask(__name__)

# provide MongoDB Atlas URL
CONNECTION_STRING = "mongodb+srv://user:<root>@cluster0.fgszvaj.mongodb.net/?retryWrites=true&w=majority"
# create connection
client = MongoClient(CONNECTION_STRING)
# find database and collection
database = client["recipes"]
collection = database["Data"]


@app.route("/enter-ingredients", methods=['POST', 'GET'])
def get_ingredients():
    #store ingredients user enters into list
    if request.method == "POST":
        create_ingredients= request.form['ingredients']
        ingredients= create_ingredients.split(',')
        # maybe need to fix to return different html
        return render_template('index.html')

    return render_template('index.html')

def get_recipes():
    # store recipes in dictionary where key:title of recipe, value:instructions for recipe
    recipes={}
    ingredients=get_ingredients
    for ingredient in ingredients:
        #access database and look for ingredient in cleaned_ingredients column
        recipe=database.cleaned_ingredients.find({ingredient})
        #add recipe to recipes dictionary
        recipes[recipe["title"]]=recipe["instructions"]
    return render_template('index.html')