#####################################################################
#     ____       ____  _________    ____  ____  __________________  #
#    / __ \_  __/ __ \/ ____/   |  / __ \/ __ )/ ____/ ____/ ____/  #
#   / / / / |/_/ / / / __/ / /| | / / / / __  / __/ / __/ / /       #
#  / /_/ />  </ /_/ / /___/ ___ |/ /_/ / /_/ / /___/ /___/ __/      #
#  \____/_/|_/_____/_____/_/  |_/_____/_____/_____/_____/_/         #
#                                                                   #
#####################################################################

import rogue
import curses
from rogue.scenes.menu import Menu

def main():
	menu = Menu()
	# Counter-intuitive naming, I know. Short on time
	selected_option = menu.draw()
	if selected_option == "HS":
		menu.print_highscore()
	elif selected_option == "MAN":
		menu.print_manual()