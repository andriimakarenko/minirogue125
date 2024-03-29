#####################################################################
#     ____       ____  _________    ____  ____  __________________  #
#    / __ \_  __/ __ \/ ____/   |  / __ \/ __ )/ ____/ ____/ ____/  #
#   / / / / |/_/ / / / __/ / /| | / / / / __  / __/ / __/ / /       #
#  / /_/ />  </ /_/ / /___/ ___ |/ /_/ / /_/ / /___/ /___/ __/      #
#  \____/_/|_/_____/_____/_/  |_/_____/_____/_____/_____/_/         #
#                                                                   #
#####################################################################

# No need for an Entity superclass, as the only thing entities share
# is having coordinates

import random

class Hero(object):
	def __init__(self, y = 0, x = 0):
		self.level = 1
		self.xp = 0
		self.hp = 16
		self.maxhp = 16
		self.strength = 16
		self.armor = 4
		self.gold = 0
		self.y = 0
		self.x = 0

	def hit(self):
		success = random.randint(0, 100)
		if success // 4 > 10:
			return True
		else:
		 	return False