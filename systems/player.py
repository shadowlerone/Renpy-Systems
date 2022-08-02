from .gameobject import GameObject
from .item import Item, InventoryItem
from .inventory import Inventory
from .quests import QuestLog
from .recipe import RecipeBook, Recipe

class Player(object):
	def __init__(self):
		self.inventory = Inventory()
		self.questlog = QuestLog()
		self.recipebook = RecipeBook()

	def get_craftable(self):
		return [r for r in self.recipebook.recipes.values() if r.requirements in self.inventory]

	def get_uncraftable(self):
		return [r for r in self.recipebook.recipes.values() if not r.requirements in self.inventory]

	def craft(self, recipe):
		pass

	def add_item(self, item, count):
		self.inventory.add_item(item, count)
	def remove_item(self, item, count):
		self.inventory.remove_item(item, count)
	def start_quest(self, quest_id, quest_object):
		self.questlog.add_quest(quest_id, quest_object)
		# self.questlog

	def add_recipe(self, recipe):
		self.recipebook.add_recipe(recipe)

	def get_quest(self):
		pass

	def set_selected_quest(self, quest_id):
		pass

	def get_selected_quest(self):
		pass

	def get_items(self):
		return self.inventory.get_items()
