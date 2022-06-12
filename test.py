import unittest

from systems.database 	import *
from systems.game 		import *
from systems.gameobject import *
from systems.inventory 	import *
from systems.item 		import *
from systems.person 	import *
from systems.player 	import *
from systems.quests 	import *
from systems.recipe 	import *

class TestItem(unittest.TestCase):
	def setUp(self):
		# self.item = Item() 
		pass

	def test_init(self):
		
		with self.assertRaises(TypeError):
			item = Item()
		with self.assertRaises(TypeError):
			item = Item("id")

		item = Item("id","name","description")
		self.assertEqual(item.id, "id")
		self.assertEqual(item.name, "name")
		self.assertEqual(item.description, "description")

	def test_from_dict(self):
		item = Item.from_dict({
			"id": "id",
			"name": "name",
			"description": "description",
			"image_path": "image/path"
		})

		self.assertEqual(
			item, 
			Item("id","name","description","image/path"), 
			"Should be the same as an item built from the constructor."
		)

		self.assertEqual(item.id, "id", "The id should be 'id'.")
		self.assertEqual(item.name, "name", "The name should be 'name'.")
		self.assertEqual(item.description, "description", "The description should be 'description'")
		self.assertEqual(item.image_path, "image/path", "The image path should be 'image/path'")


		item2 = Item.from_dict({
			"name": "name",
			"description": "description",
			"image_path": "image/path"
		})

		self.assertEqual(item2.id, "name", "The id should be 'name'.")
		self.assertEqual(item2.name, "name", "The name should be 'name'.")
		self.assertEqual(item2.description, "description", "The description should be 'description'")
		self.assertEqual(item2.image_path, "image/path", "The image path should be 'image/path'")


		item3 = Item.from_dict({
			"name": "name",
			"description": "description",
		})

		self.assertEqual(item3.id, "name", "The id should be 'name'.")
		self.assertEqual(item3.name, "name", "The name should be 'name'.")
		self.assertEqual(item3.description, "description", "The description should be 'description'")
		self.assertEqual(item3.image_path, "items/name", "The image path should be 'items/name'")

		item4 = Item.from_dict({
			"id":"id",
			"name": "name",
			"description": "description",
		})
		self.assertEqual(item4.id, "id", "The id should be 'name'.")
		self.assertEqual(item4.name, "name", "The name should be 'name'.")
		self.assertEqual(item4.description, "description", "The description should be 'description'")
		self.assertEqual(item4.image_path, "items/id", "The image path should be 'items/id'")

class TestInventoryItem(unittest.TestCase):
	def setUp(self):
		self.item = Item("id","name","description","image/path")
		self.ii = InventoryItem.from_item(self.item)
		
	def test_inventory_item_from_item(self):
		with self.assertRaises(TypeError):
			InventoryItem.from_item(1)
		with self.assertRaises(TypeError):
			InventoryItem.from_item('test')
		with self.assertRaises(TypeError):
			InventoryItem.from_item({
			"id": "id",
			"name": "name",
			"description": "description",
			"image_path": "image/path"
		})

	def test_from_item_count(self):
		ii = InventoryItem.from_item(self.item, 2)
		self.assertEqual(ii.count, 2)
	
	def test_init(self):
		self.assertEqual(self.ii.count, 0)

	def test_inventory_item_from_dict(self):
		d = {
			"id": "id",
			"name": "name",
			"description": "description",
			"image_path": "image/path"
		}
		item = Item("id","name","description","image/path")

		# TODO:
		# - test TypeError

		dict_item = Item.from_dict(d)

		ii = InventoryItem.from_dict(d)
		self.assertEqual(ii, InventoryItem.from_item(dict_item), "Generating from a dictionary should yield the same result as generating from an item generated from the same dictionary.")


	def test_set_count(self):
		self.assertEqual(self.ii.count, 0)

		self.ii.set_count(1)
		self.assertEqual(self.ii.count, 1)

		self.ii.set_count(100000)
		self.assertEqual(self.ii.count, 100000)

		with self.assertRaises(ValueError):
			self.ii.set_count(-5)

		with self.assertRaises(TypeError):
			self.ii.set_count('seven')
		
	def test_iadd(self):
		self.ii += 1

		self.assertEqual(self.ii.count, 1)

		with self.assertRaises(TypeError):
			self.ii += 'rose'
		
		with self.assertRaises(ValueError):
			self.ii += -3
		

	def test_isub(self):
		with self.assertRaises(ValueError):
			self.ii -= 1
		
		self.ii += 2
		self.ii -= 1

		self.assertEqual(self.ii.count, 1, "0 + 2 - 1 = 1")

		with self.assertRaises(ValueError):
			self.ii -= 2
		
		with self.assertRaises(TypeError):
			self.ii -= 'rose'
		
		with self.assertRaises(ValueError):
			self.ii -= 3

class TestPlaceholderInventoryItem(unittest.TestCase):
	def setUp(self):
		self.ii = PlaceholderInventoryItem("id")
	
	def test_init(self):
		self.assertEqual(self.ii.count, 0)
	def test_init_count(self):
		ii = PlaceholderInventoryItem("id", count=1)
		self.assertEqual(ii.count, 1)
	def test_set_count(self):
		self.assertEqual(self.ii.count, 0)

		self.ii.set_count(1)
		self.assertEqual(self.ii.count, 1)

		self.ii.set_count(100000)
		self.assertEqual(self.ii.count, 100000)

		with self.assertRaises(ValueError):
			self.ii.set_count(-5)

		with self.assertRaises(TypeError):
			self.ii.set_count('seven')
		
	def test_iadd(self):
		self.ii += 1

		self.assertEqual(self.ii.count, 1)

		with self.assertRaises(TypeError):
			self.ii += 'rose'
		
		with self.assertRaises(ValueError):
			self.ii += -3
		

	def test_isub(self):
		with self.assertRaises(ValueError):
			self.ii -= 1
		
		self.ii += 2
		self.ii -= 1

		self.assertEqual(self.ii.count, 1, "0 + 2 - 1 = 1")

		with self.assertRaises(ValueError):
			self.ii -= 2
		
		with self.assertRaises(TypeError):
			self.ii -= 'rose'
		
		with self.assertRaises(ValueError):
			self.ii -= 3


class TestInventory(unittest.TestCase):
	def setUp(self):
		self.item = Item("id","name","description","image/path")
		self.inventory = Inventory()
	
	def test_init(self):
		self.assertDictEqual(self.inventory.items, {}, 
			"Inventory should be empty on init")
		self.assertEqual(self.inventory.current_item, 
			InventoryItem("Nothing", "I should look at something first...", 0))

		self.assertNotEqual(self.inventory.current_item, 
			Item("Nothing", "I should look at something first..."))

	def test_add_item(self):
		self.inventory.add_item("id")
		self.assertEqual(self.inventory.items['id'].count, 1, "Adding without argument should make count 1")
		self.inventory.add_item("id")
		self.assertEqual(self.inventory.items['id'].count, 2, "Adding without argument should make count 1")

	def test_add_several_items(self):
		x = 4
		self.inventory.add_item("id",x)
		self.assertEqual(self.inventory.items['id'].count, x)
		self.inventory.add_item("id",x)
		self.assertEqual(self.inventory.items['id'].count, x*2)

	def test_add_negative_items(self):
		x = -4
		with self.assertRaises(ValueError):
			self.inventory.add_item("id",x)

	def test_remove_item(self):
		self.inventory.add_item("id")
		self.assertEqual(self.inventory.items['id'].count, 1)
		self.inventory.remove_item("id")
		self.assertEqual(self.inventory.items['id'].count, 0)
	
	def test_remove_below_zero(self):
		self.inventory.add_item("id", 0)
		with self.assertRaises(ValueError):
			self.inventory.remove_item('id')

	def test_remove_after_addition(self):
		self.inventory.add_item("id", 2)
		with self.assertRaises(ValueError):
			self.inventory.remove_item('id',3)

	def test_remove_negative_count(self):
		self.inventory.add_item("id", 2)
		with self.assertRaises(ValueError):
			self.inventory.remove_item('id',-3)
	
	def test_getitem(self):
		self.inventory.add_item("id", 2)
		self.assertEqual(self.inventory['id'].count, 2, "Getting count using [] should be 2")
		self.assertEqual(self.inventory['id'].count, self.inventory.items['id'].count, "Getting count using [] should be the same as getting count through inventory.items['id'].count")

	def test_in(self):
		self.inventory.add_item("id", 2)

		self.assertTrue("id" in self.inventory)

	def test_in_dict(self):
		self.inventory.add_item("id", 2)
		self.assertTrue({"id": 'id', 'count': 2} in self.inventory)
		self.assertFalse({"id": "id", "count":3} in self.inventory)

	def test_in_tuple(self):
		self.inventory.add_item("id", 2)
		self.assertTrue(("id", 2) in self.inventory)
		self.assertFalse(("id", 3) in self.inventory)
	
	def test_in_list_tuple(self):
		self.inventory.add_item("id", 2)
		self.inventory.add_item("name", 4)
		self.inventory.add_item("george", 1)

		self.assertTrue([
			("id", 2), 
			("name", 1),
			("george", 1)
		] in self.inventory)
		self.assertTrue([
			("id", 2), 
			("name", 1),
		] in self.inventory)
		self.assertTrue([
			("id", 2), 
		] in self.inventory)

		self.assertFalse([
			("id", 3), 
			("name", 1),
			("george", 1)
		] in self.inventory)
		self.assertFalse([
			("id", 2), 
			("name", 5),
			("george", 1)
		] in self.inventory)
		self.assertFalse([
			("id", 2), 
			("name", 3),
			("george", 2)
		] in self.inventory)

		self.assertFalse([
			("id", 4), 
			("name", 8),
		] in self.inventory)
		self.assertFalse([
			("id", 12), 
		] in self.inventory)



class TestPlayer(unittest.TestCase):
	def setUp(self):
		self.player = Player()
	# def test_init(self):
	# 	self.assertEqual(self.player.inventory, Inventory())
	# 	self.assertEqual(self.player.questlog, QuestLog())
	# 	self.assertEqual(self.player.recipebook, RecipeBook())

if __name__ == "__main__":
	unittest.main()