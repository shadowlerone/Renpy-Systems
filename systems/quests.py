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
		self.finished = False
		# if final_stage == None:
		# 	self.final_stage = len(stages)
		# else:
		# 	self.final_stage = final_stage

	def start(self, stage=None):
		self.started = True
		if stage == None:
			self.current_stage = self.start_stage
		else:
			self.current_stage = stage

	def get_stage(self, stage= None):
		if stage == None:
			return self.stages[self.current_stage]
		else:
			return self.stages[stage]

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
	def __init__(self, id, parent_quest_id, name='', description='', next_stage=0, substages = []):
		super(QuestStage, self).__init__(".".join(parent_quest_id, id),name, description)
		completed = False
		self.substages = substages

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