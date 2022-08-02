from .gameobject import GameObject

class Item(GameObject):
	def __init__(self, id, name, description= '', image_path='', icon_path = ""):
		super(Item, self).__init__(id, name, description)
		self.image_path = image_path
		self.icon_path = icon_path
	def __str__(self):
		return self.name
	@staticmethod
	def from_dict(d):
		if 'id' in d:
			id = d['id']
		else:
			id = d['name']
		
		if 'image_path' in d:
			ip = d['image_path']
		else:
			ip = "items/{}".format(id)
		return Item(id, d['name'], d['description'], image_path=ip)

class InventoryItem(Item):
	def __init__(self,id,  name, description='', image_path='', count = 0):
		super(InventoryItem, self).__init__(id, name, description, image_path)
		if count < 0:
			raise ValueError("Count cannot be less than 0")
		self.count = count
	
	def set_count(self, count):
		if not isinstance(count, int):
			raise TypeError("{} is of type {}, not {}".format(count, type(count), int))
		if count < 0:
			raise ValueError("Count cannot be less than 0")
		
		self.count = count
	def __iadd__(self, other):
		if not isinstance(other, int):
			raise TypeError("{} is of type {}, not {}".format(other, type(other), int))

		if other < 0:
			raise ValueError("Can't add negative number of items".format(other, self.count))

		self.count += other
		return self
	
	def __isub__(self, other):
		if not isinstance(other, int):
			raise TypeError("{} is of type {}, not {}".format(other, type(other), int))

		if other < 0:
			raise ValueError("Can't remove a negative number of items".format(other, self.count))
		if self.count - other < 0:
			raise ValueError("Removing {} to current count ({}) will result in a count less than 0".format(other, self.count))
		
		self.count -= other
		return self

	@staticmethod
	def from_item(item, count = 0):
		if not isinstance(item, Item):# if type(item) != Item:
			raise TypeError("{} is of type {}, not {}".format(item, type(item), Item))
		
		return InventoryItem(item.id, item.name, item.description, item.image_path, count)
	
	@staticmethod
	def from_dict(d):
		if not isinstance(d, dict):
			raise TypeError("{} is of type {}, not {}".format(d, type(d), dict))
		return InventoryItem.from_item(super(InventoryItem, InventoryItem).from_dict(d))

class PlaceholderInventoryItem(InventoryItem):
	def __init__(self,id, count=0):
		super(PlaceholderInventoryItem, self).__init__(id, "placeholder", "placeholder", "placeholder", count=count)