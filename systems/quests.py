from .gameobject import GameObject

class Quest(GameObject):
	def __init__(
			self,
			id, 
			name, 
			description, 
			stages=[],
			first_stage=None,
			final_stage=None,
		):
		super(Quest, self).__init__(id, name, description)
		self.stages = {}
		for qs in stages:
			self.stages[qs.id] = qs
		self.current_stage = 0
		self.started = False
		self.complete = False
		self.first_stage = first_stage
		self.final_stage = final_stage
		# if final_stage == None:
		# 	self.final_stage = len(stages)
		# else:
		# 	self.final_stage = final_stage

	def start(self, stage=None):
		self.started = True
		if stage == None:
			self.current_stage = self.first_stage
		else:
			self.current_stage = stage

	def get_stage(self, stage= None):
		if stage == None:
			return self.stages[".".join([self.id, str(self.current_stage)])]
		else:
			return self.stages[".".join([self.id, str(stage)])]

	def next_stage(self):
		self.stage += 1

	@staticmethod
	def from_dict(d):
		return Quest(
			d['id'],
			d['name'], 
			d['description'], 
			stages=[QuestStage.from_dict(s) for s in d['stages']],
			first_stage=d['first_stage'],

			)

class QuestStage(GameObject):
	def __init__(
		self, 
		id, 
		parent_quest_id, 
		name='', 
		description='', 
		next_stage=0, 
		substages = [],
		requirements= {}
	):
		super(QuestStage, self).__init__(".".join([parent_quest_id, str(id)]),name, description)
		self.complete = False
		for ss in substages:
			pass
		self.substages = substages
		self.requirements = requirements

	def __str__(self):
		return self.name


	@staticmethod
	def from_dict(d):
		return QuestStage(name=d['name'], description=d['description'])

class QuestLog(object):
	def __init__(self):
		self.quests = {}
	
	def get_quest(self, id):
		return self.quests[id]

	def add_quest(self, id, quest):
		self.quests[id] = quest
		self.quests[id].start()

	def get_active(self):
		qs = [q.get_stage() for q in self.quests.values() if (q.started and not q.complete)]
		sq = [q.substages for q in qs]
		# python is objectively a stupid language. This is just to flatten a list. Fuck's sake.
		return qs + [s for sublist in sq for s in sublist]

	def __getitem__(self, key):
		return self.quests[key]