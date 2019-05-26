#####################################################################
#     ____       ____  _________    ____  ____  __________________  #
#    / __ \_  __/ __ \/ ____/   |  / __ \/ __ )/ ____/ ____/ ____/  #
#   / / / / |/_/ / / / __/ / /| | / / / / __  / __/ / __/ / /       #
#  / /_/ />  </ /_/ / /___/ ___ |/ /_/ / /_/ / /___/ /___/ __/      #
#  \____/_/|_/_____/_____/_/  |_/_____/_____/_____/_____/_/         #
#                                                                   #
#####################################################################

# Item will be a superclass later, but now there's only one item
# supported and that's the power potion.

class Item(object):
	def __init__(self, id, y, x, symbol):
		self.id = id
		self.name = ''
		self.symbol = symbol
		self.y = y
		self.x = x

	def act(self, hero):
		pass