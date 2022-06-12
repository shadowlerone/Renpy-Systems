from .gameobject import GameObject

class Recipe(GameObject):
	def __init__(self, name, requirements, item, description=''):
		super(Recipe, self).__init__(name, description)
		self.requirements = requirements
		self.item = item
	def is_craftable(self, item_list):

		pass
		# return all([item_list[i] >= c for i, c in self.requirements.items()])

	@staticmethod
	def from_dict(d):
		return Recipe(
			d['name'], 
			item=d['item'],
			requirements=d['requirements'], 
			description=d['description'],
		)

	def __hash__(self):
		return hash((self.name, self.item))

	def __eq__(self, other):
		return (self.name, self.requirements, self.item) == (other.name, other.requirements, other.item)

class RecipeBook(object):
	def __init__(self):
		self.recipes = {}
		self.current_recipe = Recipe("Nothing here", {"not sure": 0}, None)
	def add_recipe(self, recipe_id):
		pass

	def add_recipe(self, recipe):
		self.recipes.add(recipe)
		for r in recipe.requirements.keys():
			self.add_item(r, 0)
	def remove_recipe(self, recipe):
		self.recipes.remove(recipe)

	def get_craftable(self):
		return [i for i in self.recipes if i.is_craftable(self.items)]

	def get_uncraftable(self):
		return [i for i in self.recipes if not i.is_craftable(self.items)]

	def craft(self, recipe):
		if recipe in self.recipes:
			if recipe.is_craftable(self.items):
				self.add_item(recipe.item)
				for i, c in recipe.requirements.items():
					self.remove_item(i, c)