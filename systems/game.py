from .database import Database
from .player import Player
from .quests import Quest
class Game(object):
	def __init__(self):
		self.people = {}
		self.db  = Database()
		self.player = Player()
	# characters = {
	# 	# list of character and info
	# }

	def game_event(func):
		def wrapper(*args, **kwargs):
			print(args)
			func(*args[1:])
			args[0].update()
		return wrapper

	def setup(self,
		people = None,
		locations = None,
		from_db = None,
		fps = False
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
			complete = True
			# substages
			reqs = q.requirements
			if "substage" in reqs:
				if reqs['substage'] == 'all':
					if not all([s.complete for s in q.substages]):
						complete = False 
				if reqs['substage'] == 'any':
					if not any([s.complete for s in q.substages]):
						complete = False
			# items
			if "item" in reqs:
				# print(reqs['item'])
				items_present = [(i in self.player.inventory) for i in reqs['item']['ids']]

				if reqs['item']['all']:
					if not all(items_present):
						complete = False
				else:
					if not any(items_present):
						complete = False
			if complete:
				q.complete()
			pass
		pass


	