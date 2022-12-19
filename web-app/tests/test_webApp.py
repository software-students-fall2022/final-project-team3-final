from app import clean_input, is_ingredient, get_recipes


def test_clean_list_of_capitalized_ingredients():
    cleanOutputIngredientsList = clean_input("Cinnamon, Pistachios, Flour")
    assert cleanOutputIngredientsList == ["cinnamon", "pistachios", "flour"]

def test_clean_list_of_lowercase_ingredients():
    cleanOutputIngredientsList = clean_input("cinnamon, pistachios, flour")
    assert cleanOutputIngredientsList == ["cinnamon", "pistachios", "flour"]

def test_actual_ingredient_is_ingredient():
    isIngredient = is_ingredient("cinnamon")
    assert isIngredient == True

def test_fake_ingredient_is_ingredient():
    isIngredient = is_ingredient("2")
    assert isIngredient == False

def test_blank_ingredient_is_ingredient():
    isIngredient = is_ingredient("")
    assert isIngredient == False

'''
def test_get_recipes_with_all_real_ingredients():
    #init_test()
    # connect to the database
    try:
        # provide MongoDB Atlas URL
        CONNECTION_STRING = "mongodb+srv://user:root@cluster0.fgszvaj.mongodb.net/?retryWrites=true&w=majority"
        # create connection
        client = MongoClient(CONNECTION_STRING, 500)
        client.admin.command('ping')
    # if we get here, the connection worked!
        database = client["recipes"]
        print(' *', 'Connected to MongoDB!')
    except Exception as e:
        print(e)
    returnedRecipes = get_recipes(["cinnamon", "pistachios", "flour"], database)
    firstRecipe = returnedRecipes[0]
    nameOfFirstRecipe = firstRecipe["name"]
    assert nameOfFirstRecipe == "Pumpkin Dutch Baby With Pumpkin Butter"

def test_get_recipes_with_single_ingredient():
    #init_test()
    returnedRecipes = get_recipes(["cumin seeds"])
    firstRecipe = returnedRecipes[0]
    nameOfFirstRecipe = firstRecipe["name"]
    assert nameOfFirstRecipe == "Spiced Lentil and Caramelized Onion Baked Eggs"

def test_get_recipes_with_some_real_some_fake_ingredients():
    #init_test()
    returnedRecipes = get_recipes(["strawberry, flour, 42"])
    firstRecipe = returnedRecipes[0]
    nameOfFirstRecipe = firstRecipe["name"]
    assert nameOfFirstRecipe == "Strawberry Coconut Cake"
'''