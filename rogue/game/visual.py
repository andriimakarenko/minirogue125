#####################################################################
#     ____       ____  _________    ____  ____  __________________  #
#    / __ \_  __/ __ \/ ____/   |  / __ \/ __ )/ ____/ ____/ ____/  #
#   / / / / |/_/ / / / __/ / /| | / / / / __  / __/ / __/ / /       #
#  / /_/ />  </ /_/ / /___/ ___ |/ /_/ / /_/ / /___/ /___/ __/      #
#  \____/_/|_/_____/_____/_/  |_/_____/_____/_____/_____/_/         #
#                                                                   #
#####################################################################

import curses
import time

def start_game(window):
	window.addstr(13, 37, "Game started")
	window.refresh()


def vs_key_events(input_map, controller):
	hero_y, hero_x = controller.getheroyx()
	# [[13, 17, 'B'], [2, 28, 'K']]
	enemies = controller.getmonsters()
	input_map[0][0]
