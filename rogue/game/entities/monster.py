#####################################################################
#     ____       ____  _________    ____  ____  __________________  #
#    / __ \_  __/ __ \/ ____/   |  / __ \/ __ )/ ____/ ____/ ____/  #
#   / / / / |/_/ / / / __/ / /| | / / / / __  / __/ / __/ / /       #
#  / /_/ />  </ /_/ / /___/ ___ |/ /_/ / /_/ / /___/ /___/ __/      #
#  \____/_/|_/_____/_____/_/  |_/_____/_____/_____/_____/_/         #
#                                                                   #
#####################################################################

import random

class Monster(object):
	def __init__(self, id, y, x, letter):
		self.id = id
		self.name = ''
		self.letter = letter
		self.y = y
		self.x = x
		self.hp = 5
		self.received_hits = 0

	def hit(self):
		success = random.randint(0, 100)
		if success // 4 > 10:
			return True
		else:
		 	return False