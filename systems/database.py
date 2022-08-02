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
		self.quests = {}
		self.people = {}
		self.locations = {}
		# self.recipe_list = self.load_recipes_from_file()


	def verify(self):
		all_ids = [i.id for i in self.items.values() + self.recipes.values() + self.quests.values() + self.people.values() + self.locations.values()]
		dupes = [(i, all_ids.count(1)) for i in all_ids if all_ids.count(i) > 1]
		if len(dupes) > 0:
			raise ValueError("\n".join(["ID: {} occurs {} times in Database".format(i[0], i[1]) for i in dupes]))
		

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
	
	def get_quest(self, quest_id):
		pass


	def set_items(self, items):
		for i in items:
			self.items[i.id] = i

	def __getitem__(self, key):
		return [i for i in self.items.values() + self.recipes.values() + self.quests.values() + self.people.values() + self.locations.values() if i.id == key][0]