from flask import Flask, render_template, request, redirect, abort, url_for, make_response, flash
from pymongo import MongoClient
from dotenv import dotenv_values
import os
import recipe_logic

# global variables 
config = dotenv_values(".env")
app = Flask(__name__)
userInput = ''

# connect to the database
# don't know if we want to change this for next time 
database = None
cxn = pymongo.MongoClient("mongodb", 27017)
try:
	# verify the connection works by pinging the database
	cxn.admin.command('ping') # The ping command is cheap and does not require auth.
	#database = cxn['___'] # store a reference to the database
	print(' *', 'Connected to MongoDB!') # if we get here, the connection worked!
	
@app.route('/', methods=('GET', 'POST'))
def index():
	if request.method == "POST":
		#store ingredients user enters into list
		userInput = request.form['userInput']
		print(userInput)
		return redirect('/results', code=302)
	
	return render_template('index.html')

# display results 
@app.route('/results')
def results():
	recipe = {'img': 'img-link', 'name': 'pizza', 'spices': 'oregano, basil'}
	recipes = [recipe]
	#recipes = recipe_logic.get_recipes(userInput) <- for later
	return render_template('results.html', recipes=recipes)

# run the app
if __name__ == "__main__":
	app.run()