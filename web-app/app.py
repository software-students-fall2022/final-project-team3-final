from flask import Flask, render_template, request, redirect, abort, url_for, make_response, flash, session
from pymongo import MongoClient
#from dotenv import dotenv_values
import os

# import recipe_logic
from os.path import dirname, join
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# import recipe_logic
#sys.path("./backend-db")
#import recipe_logic
# global variables
#config = dotenv_values(".env")
app = Flask(__name__)
# userInput = ''

app.secret_key = 'BAD_SECRET_KEY'


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

def clean_input(user_input):
    out = user_input.split(',')
    for i in range(len(out)):
        out[i] = out[i].strip()
        out[i] = out[i].lower()
    return out

def is_ingredient(ingredient):
    #takes an ingredient and makes sure that it is one
    is_ingredient = True
    if len(ingredient) <= 1:  #length > 1
        is_ingredient = False
    
    is_ingredient = False
    for c in ingredient:  #makes sure that user input contains at least one letter
        if c.isalpha():
            is_ingredient = True
    return is_ingredient  
    

def get_recipes(user_ingredients):
    # store recipes in dictionary where key:title of recipe, value:instructions for recipe
    matched_recipes = []
    #database['Data'].find_one({'Cleaned_Ingredients': { '$regex' : "cumin seeds"}})
    for ingredient in user_ingredients:
        if is_ingredient(ingredient):
            for elem in database['Data'].find({'Cleaned_Ingredients': { '$regex' : ingredient}}):
            #print(elem)
                match_score = 0 #create a very crude 'cost function' to return most applicable results based on proximity to our ingredients list
                for ingredient in user_ingredients: # we want recipes where all of our ingredients are represented, not just a few
                    if ingredient in elem['Cleaned_Ingredients']:
                        match_score += 1
                    else:
                        match_score -= 1
                
                if match_score > 0: #set an arbitrary cutoff at 0 to make sure we are generally showing something
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
        #print(userInput)
        ingredients_query = clean_input(userInput)

        session['user_input'] = ingredients_query

        return redirect('/results', code=302)
    return render_template('index.html')

# display results

@app.route('/results')
def results():
    # recipe = {'img': 'img-link', 'name': 'Pizza', 'spices': 'Oregano, Basil'}
    # recipes = [recipe]
    user_input = session['user_input']
    recipes = get_recipes(user_input)
    return render_template('results.html', recipes=recipes)


# run the app
if __name__ == "__main__":
    app.run()
