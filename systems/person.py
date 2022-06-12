from .gameobject import GameObject

class Person(GameObject):
	def __init__(self, id, name, description, base_affinity):
		super(Person, self).__init__(id, name, description)
		self.base_affinity = base_affinity
		self.affinity = base_affinity
		self.location = ""
	def set_affinity(self, value):
		self.affinity = value
	def increase_affinity(self, value=1):
		self.affinity += value
	def decrease_affinity(self, value=1):
		self.affinity -= value
	def get_affinity(self):
		return self.affinity
	def __str__(self):
		return self.name

