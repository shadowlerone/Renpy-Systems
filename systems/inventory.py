from .item import InventoryItem, Item, PlaceholderInventoryItem
from .recipe import Recipe

class Inventory():
	"""
	An Inventory.

	Organizes items. It's basically a glorified list.
	"""
	def __init__(self):
		self.items = {}
		self.current_item = InventoryItem("Nothing", "I should look at something first...", 0)
		
	def add_item(self, item_id, count=1):
		"""
		Adds item to the Inventory.
		
		Arguments:
		item_id -- id or Item object of the Item to add
		count -- Amount of the Item to add (default: 1)
		"""
		if not isinstance(count, int): # if type(count) != int:
			raise TypeError("{} is of type {}, not {}".format(count, type(count), int))
		if isinstance(item_id, str) or isinstance(item_id, unicode):
			if item_id in self.items:
				self.items[item_id] += count
			else:
				self.items[item_id] = PlaceholderInventoryItem(item_id, count)
		elif isinstance(item_id, Item): # elif type(item_id) == (Item):
			if item_id.id not in self.items:
				self.items[item_id.id] = InventoryItem.from_item(item_id, count)
			else:
				self.items[item_id.id] += count
		else:
			raise TypeError("{} is of type {}, not {} or {}".format(item_id, type(item_id), str, Item))

	def remove_item(self, item, count=1):
		if item in self.items:
			self.items[item] -= count
	
	def __getitem__(self, item_id):
		return self.items[item_id]

	def __contains__(self, key):
		"""Checks if Item is in Inventory.
		
		Key can be:
		str: returns True if str matches any ids in list of items
		dict {'id': str, 'count': int}: if str is in list of items, 
			returns True if count is greater than Item.count, else False
		tuple (str, int): if str in list, returns int >= item.count, else False
		list [str, int]: same as tuple
		list [[str, int]]: for every list, same as tuple. Returns whether all are True.
		"""
		if isinstance(key, str):
			return key in self.items
		elif isinstance(key, dict):
			if key['id'] in self.items:
				return self.items[key['id']].count >= key['count']
			else:
				return False
		elif isinstance(key, tuple): #type(key) == tuple:
			if key[0] in self.items:
				return self.items[key[0]].count >= key[1]
			else:
				return False
		elif isinstance(key, list): # type(key) == list:
			if all([isinstance(i, tuple) for i in key]):
				if all([len(i) == 2 for i in key]):
					if all([i[0] in self.items for i in key]):
						return all([self.items[i[0]].count >= i[1] for i in key])
					else:
						return False
				else:
					raise ValueError("All tuples must be of types (<str>, <int>")
			elif len(key) == 2:
				if key[0] in self.items:
					return self.items[key[0]].count >= key[1]
				else:
					return False
			else:
				raise ValueError("Must be a list of tuples of types (<str>, <int>)")
		else:
			raise ValueError("Input must be of types <str>, <dict>, <tuple>, list[<str>, <int>] or list[(<str>,<int>)], not {}".format(type(key)))

	## To be rewritten. No tests written for these
	def get_items(self):
		return [i for i in self.items.values() if i.count > 0]
		# return [["{} x{}".format(i[0], i[1]), i[0]] for i in list(filter(lambda i: i[1] > 0, self.items.items()))]

	def get_item_count(self, item):
		if self.items.has_key(item):
			return self.items[item]
		return 0

	def set_current_item(self, item):
		self.current_item = item
	
	def get_current_item(self):
		return self.current_item
