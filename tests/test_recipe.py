from lib.recipe import Recipe

"""
Given an instance of Recipe is created,
recipe_name, average_cooking_time, and recipe_rating
properties are assigned
"""

def test_recipe_properties_assigned():
    recipe = Recipe(1, "Chicken Dinner", 90, 5)
    assert recipe.id == 1
    assert recipe.recipe_name == "Chicken Dinner"
    assert recipe.average_cooking_time == 90
    assert recipe.recipe_rating == 5


"""
Given 2 instances with equal properties
they are classed as equal
"""
def test_equal_recipes():
    recipe1 = Recipe(1, "Chicken Dinner", 90, 5)
    recipe2 = Recipe(1, "Chicken Dinner", 90, 5)
    assert recipe1 == recipe2

"""
We can format recipes to strings
"""

def test_format_recipe_to_string():
    recipe = Recipe(1, "Chicken Dinner", 90, 5)
    assert str(recipe) == "Recipe(1, Chicken Dinner, 90, 5)"