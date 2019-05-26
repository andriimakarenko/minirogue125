#####################################################################
#     ____       ____  _________    ____  ____  __________________  #
#    / __ \_  __/ __ \/ ____/   |  / __ \/ __ )/ ____/ ____/ ____/  #
#   / / / / |/_/ / / / __/ / /| | / / / / __  / __/ / __/ / /       #
#  / /_/ />  </ /_/ / /___/ ___ |/ /_/ / /_/ / /___/ /___/ __/      #
#  \____/_/|_/_____/_____/_/  |_/_____/_____/_____/_____/_/         #
#                                                                   #
#####################################################################

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

	def initialize(self):
		print("Empiezando la importacion")
		self.import_map()
		print("Gracias por el juego, " + self.player_name)
		print("El ID del monstruo ultimo = " + str(self.monsters[-1].id))

	def import_map(self):
		try:
			with open("rogue/levels/01", 'r') as level:
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
				elif self.map[y][x] in ['!', '*']:
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
		return ""

	#########################################################################
	#                      CONTROL REQUESTS HANDLING                        #
	#########################################################################

	def try_move(self, direction):
		y, x = self.get_target(direction)
		if self.map[y][x] in ['+', ' ']:
			return
		
		for item in self.items:
			if item.y == y and item.x == x:
				item.act(hero)
				self.items.remove(item)
				self.hero.y, self.hero.x = y, x
				return

		for monster in self.monsters:
			return

		self.hero.y, self.hero.x = y, x

	def get_target(self, direction):
		y, x = self.get_hero_yx()
		if direction == 'u':
			y -= 1
		elif direction == 'd':
			y += 1
		elif direction == 'l':
			x -= 1
		elif direction == 'r':
			x += 1
		return y, x
