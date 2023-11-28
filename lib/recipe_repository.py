from lib.recipe import Recipe

class RecipeRepository():
    def __init__(self, connection):
        self.connection = connection
    
    def all(self):
        rows = self.connection.execute('SELECT * from recipes')
        recipes = []
        for row in rows:
            item = Recipe(row['id'], row['recipe_name'], row['average_cooking_time'],row['recipe_rating'])
            recipes.append(item)
        return recipes

    def find(self, recipe_id):
        rows = self.connection.execute('SELECT * from recipes WHERE id = %s', [recipe_id] )
        row = rows[0]
        recipe = Recipe(row['id'], row['recipe_name'], row['average_cooking_time'],row['recipe_rating'])
        return recipe