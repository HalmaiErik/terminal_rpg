import random
from .magic import Spell

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

class Person:
	def __init__(self, hp, mp, atk, df, magic, items):
		self.max_hp = hp
		self.hp = hp
		self.max_mp = mp
		self.mp = mp
		self.atk_low = atk - 10
		self.atk_high = atk + 10
		self.df = df
		self.magic = magic
		self.items = items
		self.actions = ["Attack", "Magic", "Items"]

	def generate_dmg(self):
		return random.randrange(self.atk_low, self.atk_high)

	def take_dmg(self, dmg):
		self.hp -= dmg
		if self.hp < 0:
			self.hp = 0
		return self.hp

	def reduce_mp(self, cost):
		self.mp -= cost

	def heal(self, health):
		self.hp += health
		if self.hp > self.max_hp:
			self.hp = self.max_hp

	def restore_mp(self, magic):
		self.mp += magic
		if self.mp > self.max_mp:
			self.mp = self.max_mp

	def choose_action(self):
		i = 1
		print("\nActions:")
		for action in self.actions:
			print("    " + str(i) + ".", action)
			i += 1

	def choose_magic(self):
		i = 1
		print("\nSpells:")
		for spell in self.magic:
			print("    " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
			i += 1

	def choose_item(self):
		i = 1
		print("\nItems:")
		for item in self.items:
			print("    " + str(i) + ".", item["item"].name, ":", item["item"].desc, "x" + str(item["quantity"]))
			i += 1

	def get_hp(self):
		return self.hp

	def get_max_hp(self):
		return self.max_hp

	def get_mp(self):
		return self.mp

	def get_max_mp(self):
		return self.max_mp