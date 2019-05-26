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
		self.legit_coordinates = []
		self.lighted_zones = []

	def initialize(self):
		# print("Empiezando la importacion")
		# print("Gracias por el juego, " + self.player_name)

	def import_map(self):
		with open("rogue/levels/01", 'r') as level:
			self.map = readlines(level)
		for y in range(len(map)):
			for x in range(len(map[y])):
				if map[y][x] not in [' ', '—', '|']:
					self.legit_coordinates.append((y, x))
				if map[y][x] == '@':
					self.hero.y, self.hero.x = y, x
				elif map[y][x] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
					monster = Monster(y, x, map[y][x])
					self.monsters.append(monster)
				elif map[y][x] in ['!', '*']:
					item = Item(y, x, map[y][x])
					self.items.append(item)
