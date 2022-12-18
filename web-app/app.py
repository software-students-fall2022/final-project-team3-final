from flask import Flask, render_template, request, redirect, abort, url_for, make_response, flash
from pymongo import MongoClient
from dotenv import dotenv_values
import os

# import recipe_logic
from os.path import dirname, join
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# import recipe_logic
#sys.path("./backend-db")
#import recipe_logic

# global variables
config = dotenv_values(".env")
app = Flask(__name__)
# userInput = ''

# connect to the database
try:
    # provide MongoDB Atlas URL
    CONNECTION_STRING = "mongodb+srv://user:root@cluster0.fgszvaj.mongodb.net/?retryWrites=true&w=majority"
    # create connection
    client = MongoClient(CONNECTION_STRING, 500)
# verify the connection works by pinging the database
# The ping command is cheap and does not require auth.
    client.admin.command('ping')
# if we get here, the connection worked!
    database = client["recipes"]
    collection = database["Data"]
    print(' *', 'Connected to MongoDB!')
except Exception as e:
    print(e)

def get_recipes(user_ingredients):
    # store recipes in dictionary where key:title of recipe, value:instructions for recipe
    matched_recipes = []

    #database['Data'].find_one({'Cleaned_Ingredients': { '$regex' : "cumin seeds"}})
    for ingredient in user_ingredients:
        for elem in database['Data'].find({'Cleaned_Ingredients': { '$regex' : ingredient}}):
            #print(elem)
            matched_recipes.append(
                {'img': elem['Image_Name'], 'name': elem['Title'], 'ingredients': elem['Cleaned_Ingredients']})            

    #print(database.collection.stats())
    #for ingredient in user_ingredients:
        # access database and look for ingredient in cleaned_ingredients column
        #recipe = database.cleaned_ingredients.find_one(ingredient)

        # add recipe to recipes dictionary
        # matched_recipes.append(
        #     {'name': recipe['title'], 'instructions': recipe['instructions']})
    return matched_recipes

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == "POST":
        # store ingredients user enters into list
        userInput = request.form['userInput']
        print(userInput)
        return redirect('/results', code=302)
    return render_template('index.html')

# display results


@app.route('/results')
def results():
    # recipe = {'img': 'img-link', 'name': 'Pizza', 'spices': 'Oregano, Basil'}
    # recipes = [recipe]
    user_input = ['cumin seeds']
    recipes = get_recipes(user_input)
    return render_template('results.html', recipes=recipes)


# run the app
if __name__ == "__main__":
    app.run()
