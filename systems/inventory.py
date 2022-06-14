from .item import InventoryItem, Item, PlaceholderInventoryItem
from .recipe import Recipe

class Inventory():
	def __init__(self):
		self.items = {}
		self.current_item = InventoryItem("Nothing", "I should look at something first...", 0)
		
	def add_item(self, item_id, count=1):
		if type(count) != int:
			raise TypeError("{} is of type {}, not {}".format(item_id, type(item_id), int))
		if type(item_id) == str:
			if item_id in self.items:
				self.items[item_id] += count
			else:
				self.items[item_id] = PlaceholderInventoryItem(item_id, count)
		elif type(item_id) == (Item):
			self.items[item_id.id] = InventoryItem.from_item(item_id, count)
		else:
			raise TypeError("{} is of type {}, not {} or {}".format(item_id, type(item_id), str, Item))

	def remove_item(self, item, count=1):
		if item in self.items:
			self.items[item] -= count
	
	def __getitem__(self, item_id):
		return self.items[item_id]

	def __contains__(self, key):
		if type(key) == str:
			return key in self.items
		elif type(key) == dict:
			if key['id'] in self.items:
				return self.items[key['id']].count >= key['count']
			else:
				return False
		elif type(key) == tuple:
			if key[0] in self.items:
				return self.items[key[0]].count >= key[1]
			else:
				return False
		elif type(key) == list:
			if all([type(i) == tuple for i in key]):
				if all([len(i) == 2 for i in key]):
					return all([self.items[i[0]].count >= i[1] for i in key])
				else:
					raise ValueError("All tuples must be of types (<str>, <int>")
			elif len(key) == 2:
				return self.items[key[0]].count >= key[1]
			else:
				raise ValueError("Must be a list of tuples of types (<str>, <int>)")
		else:
			raise ValueError("Input must be of types <str>, <dict>, <tuple>, list[<str>, <int>] or list[(<str>,<int>)]")

	## To be rewritten. No tests written for these
	def get_items(self):
		return [["{} x{}".format(i[0], i[1]), i[0]] for i in list(filter(lambda i: i[1] > 0, self.items.items()))]

	def get_item_count(self, item):
		if self.items.has_key(item):
			return self.items[item]
		return 0

	def set_current_item(self, item):
		self.current_item = item
	
	def get_current_item(self):
		return self.current_item
