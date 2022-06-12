import json
import os.path as path
from .item import Item
from .recipe import Recipe, RecipeBook
class Database(object):
	def __init__(
		self,
		directory='data', 
		item_fp='items.json', 
		recipe_fp='recipes.json'
	):
		self.directory, self.items_fp, self.recipes_fp = directory, item_fp, recipe_fp
		# self.item_list = self.load_items_from_file()
		self.items = {}
		self.recipes = {}
		# self.recipe_list = self.load_recipes_from_file()

	def load_items_from_file(self, file):
		data = json.load(file)
		items = {}
		for i in data:
			items[i['id'] if 'id' in i else i['name'].lower()] = Item.from_dict(i)
		self.items = items

	def load_recipes_from_file(self, file):
		data = json.load(file)
		recipes = {}
		for r in data:
			recipes[r['id'] if 'id' in r else r['name'].lower()] = Recipe.from_dict(r)
		self.recipes = recipes
	
	def get_item(self, item_id=''):
		return self.item_list[item_id]

	def get_recipe(self, recipe_id=''):
		return self.recipes[recipe_id]