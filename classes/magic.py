import random

class Spell:
	def __init__(self, name, cost, dmg, type):
		self.name = name
		self.cost = cost
		self.dmg = dmg
		self.type = type

	def generate_dmg(self):
		dmg_low = self.dmg - 15
		dmg_high = self.dmg + 15
		return random.randrange(dmg_low, dmg_high)