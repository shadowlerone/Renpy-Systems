from .gameobject import GameObject
from .item import Item, InventoryItem
from .inventory import Inventory
from .quests import QuestLog
from .recipe import RecipeBook

class Player(object):
	def __init__(self):
		self.inventory = Inventory()
		self.questlog = QuestLog()
		self.recipebook = RecipeBook()

	def get_craftable(self):
		pass

	def get_uncraftable(self):
		pass

	def craft(self, recipe):
		pass