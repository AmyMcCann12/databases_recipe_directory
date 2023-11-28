from lib.recipe_repository import *

"""
When we call RecipeRepository#all
we get a list of Recipe Objects reflecting the seed data
"""

def test_get_all_recipe_records(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)
    recipes = repository.all()
    assert recipes == [
        Recipe(1,'Cottage Pie', 60, 5),
        Recipe(2,'Cheese on Toast', 5, 3),
        Recipe(3,'Beef Stew', 90, 4),
        Recipe(4,'Tomatoe Soup', 7, 3),
        Recipe(5,'Pasta Bake', 30, 4)
    ]

"""
When we call RecipeRepository #find
we can find a specific recipe object
"""

def test_find_a_recipe_record(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)
    recipe = repository.find(4)
    assert recipe == Recipe(4,'Tomatoe Soup', 7, 3)