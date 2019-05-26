#####################################################################
#     ____       ____  _________    ____  ____  __________________  #
#    / __ \_  __/ __ \/ ____/   |  / __ \/ __ )/ ____/ ____/ ____/  #
#   / / / / |/_/ / / / __/ / /| | / / / / __  / __/ / __/ / /       #
#  / /_/ />  </ /_/ / /___/ ___ |/ /_/ / /_/ / /___/ /___/ __/      #
#  \____/_/|_/_____/_____/_/  |_/_____/_____/_____/_____/_/         #
#                                                                   #
#####################################################################

import random
from rogue.game.entities.hero import Hero
from rogue.game.entities.monster import Monster
from rogue.game.entities.item import Item

class Controller(object):
	def __init__(self, name):
		self.player_name = name
		if len(name) == 0:
			self.player_name = "Player One"
		self.hero = Hero()
		self.monsters = []
		self.items = []
		self.map = []
		self.rooms = [] # ID, upper left, and lower right in each
		self.inventory = []
		self.lighted_zones = []
		self.message = ''

	def initialize(self):
		self.import_map()

	def import_map(self):
		try:
			with open("rogue/levels/02", 'r') as level:
				self.map = level.readlines()
		except IOError:
			print("All went to hell")
		for y in range(len(self.map)):
			for x in range(len(self.map[y])):
				if self.map[y][x] == '@':
					self.hero.y, self.hero.x = y, x
				elif self.map[y][x] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
					monster = Monster(len(self.monsters), y, x, self.map[y][x])
					self.monsters.append(monster)
				elif self.map[y][x] in ['!', '*', '%']:
					item = Item(len(self.items), y, x, self.map[y][x])
					self.items.append(item)

	#########################################################################
	#                           GIVE OUT INFO                               #
	#########################################################################

	def get_hero_hp(self):
		return self.hero.hp

	def get_hero_yx(self):
		return self.hero.y, self.hero.x

	def get_monsters(self):
		result = []
		for monster in self.monsters:
			result.append([monster.y, monster.x, monster.letter])
		return result

	def get_items(self):
		result = []
		for item in self.items:
			result.append([item.y, item.x, item.symbol])
		return result

	def is_lighted(self, y, x):
		return True

	def get_message(self):
		output = self.message
		self.message = ''
		return output

	def get_status(self):
		result = ''
		result = "Level: {lvl}, ".format(lvl = self.hero.level)
		result += "Gold: {gold}, ".format(gold = self.hero.gold)
		result += "HP: {hp}({hpmax}), ".format(hp = self.hero.hp, hpmax = self.hero.maxhp)
		result += "Strength: {str}, ".format(str = self.hero.strength)
		result += "Armor: {arm}, ".format(arm = self.hero.gold)
		result += "XP: {xp}". format(xp = self.hero.xp)
		return result

	#########################################################################
	#                      CONTROL REQUESTS HANDLING                        #
	#########################################################################

	def try_move(self, direction):
		y, x = self.hero.y, self.hero.x
		if direction == 'u':
			y -= 1
		if direction == 'd':
			y += 1
		if direction == 'l':
			x -= 1
		if direction == 'r':
			x += 1

		if self.map[y][x] in ['+', ' ']:
			return

		for item in self.items:
			if item.y == y and item.x == x:
				if item.symbol == '*':
					self.hero.gold += random.randint(1, 50)
				if item.symbol == '!':
					self.hero.strength += 5
				if item.symbol == '%':
					self.hero.hp = -1337
				self.items.remove(item)
				self.hero.y, self.hero.x = y, x
				return

		for monster in self.monsters:
			if monster.y == y and monster.x == x:
				if self.hero.hit():
					self.message += "You've hit a monster. "
					monster.hp -= self.hero.strength // 5
					monster.received_hits += 1
				else:
					self.message += "You've missed a hit on a monster. "
				if monster.hit():
					self.message += "A monster hit you. "
					self.hero.hp -= 5
				else:
					self.message += "A monster missed his hit on you."
				if monster.hp < 1:
					self.message = "You've defeated a monster"
					self.monsters.remove(monster)
					self.hero.xp += monster.received_hits
				return

		self.hero.y, self.hero.x = y, x