from pymongo import MongoClient
from flask import Flask, request, render_template
from dotenv import dotenv_values

#app= Flask(__name__)

# provide MongoDB Atlas URL
CONNECTION_STRING = "mongodb+srv://user:<root>@cluster0.fgszvaj.mongodb.net/?retryWrites=true&w=majority"
# create connection
client = MongoClient(CONNECTION_STRING)
# find database and collection
database = client["recipes"]
collection = database["Data"]

''' Commented out accidental front-end code
@app.route("/enter-ingredients", methods=['POST', 'GET'])
def get_ingredients():
    #store ingredients user enters into list
    if request.method == "POST":
        create_ingredients= request.form['ingredients']
        ingredients= create_ingredients.split(',')
        # maybe need to fix to return different html
        return render_template('index.html', ingredients=ingredients)

    return render_template('index.html')
'''
def get_recipes(user_ingredients):
    # store recipes in dictionary where key:title of recipe, value:instructions for recipe
    matched_recipes = []
    for ingredient in user_ingredients:
        #access database and look for ingredient in cleaned_ingredients column
        recipe = database.cleaned_ingredients.find_one({ingredient})
        #add recipe to recipes dictionary
        matched_recipes.append({'name': recipe['title'], 'instructions': recipe['instructions']})
    return matched_recipes