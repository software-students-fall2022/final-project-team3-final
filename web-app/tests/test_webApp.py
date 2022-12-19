from app import clean_input, is_ingredient, get_recipes, app
import json
import pytest


def test_clean_list_of_capitalized_ingredients():
    cleanOutputIngredientsList = clean_input("Cinnamon, Pistachios, Flour")
    assert cleanOutputIngredientsList == ["cinnamon", "pistachios", "flour"]

def test_clean_list_of_lowercase_ingredients():
    cleanOutputIngredientsList = clean_input("cinnamon, pistachios, flour")
    assert cleanOutputIngredientsList == ["cinnamon", "pistachios", "flour"]

def test_clean_input_returntype():
        assert isinstance(clean_input("egg,cumin"), list) , "did not return list"

def test_is_ingredient_returntype():
    assert isinstance(is_ingredient("ingredient"), bool)

def test_actual_ingredient_is_ingredient():
    isIngredient = is_ingredient("cinnamon")
    assert isIngredient == True

def test_fake_ingredient_is_ingredient():
    isIngredient = is_ingredient("2")
    assert isIngredient == False

def test_blank_ingredient_is_ingredient():
    isIngredient = is_ingredient("")
    assert isIngredient == False

def test_index_route():
    response = app.test_client().get('/')
    assert response.status_code == 200