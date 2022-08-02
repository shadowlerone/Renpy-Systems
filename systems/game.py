from .database import Database
from .player import Player
from .quests import Quest
from .recipe import Recipe
class Game(object):
	def __init__(self):
		self.people = {}
		self.db  = Database()
		self.player = Player()
	# characters = {
	# 	# list of character and info
	# }
	def setup(self,
		people = None,
		locations = None,
		from_db = False,
		fps = {},
		items = [],
		recipes = [],
		quests = []
	):
		if from_db:
			return
			self.db.load_items_from_file(fps['items'])
			self.db.load_recipes_from_file(fps['recipes'])
		else:
			if people:
				self.people = people
			if locations:
				self.location = locations
			if items:
				self.db.set_items(items)
			if recipes:
				for i in recipes:
					self.db.recipes[i.id] = i
			if quests:
				for i in quests:
					self.db.quests[i.id] = i
	# @game_event	
	def start_quest(self, quest_id= None, quest_object = None):
		if not (isinstance(quest_id, str) or type(quest_id) != None):
			raise TypeError("quest_id is not a <str>, is type {}".format(type(quest_id)))
		if not (isinstance(quest_object, Quest) or type(quest_object) != None):
			raise TypeError("quest_object is not a <Quest>")
		if quest_id and not quest_object:
			self.player.start_quest(quest_id, self.db.get_quest(quest_id))
		elif quest_id and quest_object:
			self.player.start_quest(quest_id, quest_object)
		elif quest_object:
			self.player.start_quest(quest_object.id, quest_object)
		else:
			raise ValueError()
		self.update()
	
	


	def update(self):
		self.update_quests()
		pass

	def update_quests(self):
		for q in self.player.questlog.get_active():
			stage = q.get_stage()
			stage_complete = True

			# TODO: implement stage check logic
			for substage in stage.substages:
				r = substage.requirements
				complete = True
				if "item" in r:
					# print(reqs['item'])
					items_present = [(i in self.player.inventory) for i in r['item']['ids']]
					if r['item']['all']:
						if not all(items_present):
							complete = False
					else:
						if not any(items_present):
							complete = False
				if complete:
					substage.complete = True

			reqs = stage.requirements
			if "substage" in reqs:
				completed_stages = [s.complete for s in stage.substages]
				if reqs['substage'] == 'all':
					if not all(completed_stages):
						stage_complete = False 
				if reqs['substage'] == 'any':
					if not any(completed_stages):
						stage_complete = False
			if "item" in reqs:
				# print(reqs['item'])
				items_present = [(i in self.player.inventory) for i in reqs['item']['ids']]
				if reqs['item']['all']:
					if not all(items_present):
						stage_complete = False
				else:
					if not any(items_present):
						stage_complete = False
			if stage_complete:
				stage.complete = True
				q.next_stage()

	def set_selected_quest(self, quest_id):
		self.player.questlog.set_selected_quest(quest_id)

	def get_selected_quest(self):
		return self.player.questlog.selected_quest

	def add_item(self, item, count= 1):
		self.player.add_item(item, count)
		self.update()
	def remove_item(self, item, count= 1):
		self.player.remove_item(item, count)
		self.update()
	
	def craft(self, recipe):
		if isinstance(recipe, str):
			if recipe in [r.id for r in self.get_craftable()]:
				for req in recipe.requirements:
					self.remove_item(req[0], req[1])
				for i in recipe.items:
					self.add_item(self.db[i[0]], i[1])
		elif isinstance(recipe, Recipe):
			if recipe in self.get_craftable():
				for req in recipe.requirements:
					self.remove_item(req[0], req[1])
				for i in recipe.items:
					self.add_item(self.db[i[0]], i[1])

		else:
			raise TypeError("Must be of type <str> or <Recipe>, not {}".format(type(recipe)))
		self.update()


	def get_craftable(self):
		return self.player.get_craftable()
	
	def get_uncraftable(self):
		return self.player.get_uncraftable()


	