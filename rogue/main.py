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
from rogue.game.controller import Controller

def main():
	player_name = input("What's ur name, playa? ")
	menu = Menu()
	# Counter-intuitive naming, I know. Short on time
	selected_option = menu.draw()
	if selected_option == "HS":
		menu.print_highscore()
	elif selected_option == "MAN":
		menu.print_manual()
	elif selected_option == "P":
		controller = Controller(player_name)
		controller.initialize()
	print(selected_option)