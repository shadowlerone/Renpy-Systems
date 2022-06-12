class GameObject(object):
	def __init__(self, id, name='', description=''):
		self.id = id
		self.name = name
		self.description = description
	def __repr__(self):
		return "<{} id='{}' name='{}' desc='{}'>".format(
			self.__class__.__name__,
			self.id,
			self.name, 
			self.description
			)

	def __hash__(self):
		return hash((self.name, self.description))
	
	def __eq__(self, other):
		return (self.id,self.name, self.description, self.__class__.__name__) == (other.id,other.name, other.description, other.__class__.__name__)
	
	def __ne__(self, other):
		return not(self == other)

