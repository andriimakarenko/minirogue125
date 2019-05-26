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
from rogue.game.visualtest import vs_main

def parser_txt(filename):
    array = []

    repl_to = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    repl_to.extend([chr(i) for i in range(ord('A'), ord('Z') + 1)])
    repl_to.extend(['@', '!', '*'])

    with open(filename, 'r') as f:
        data = f.readlines()

    for line in data:
        new_line = ''.join(['.' if ch in repl_to else ch for ch in line]).rstrip()
        array.append(new_line)
    return array

def main():
	player_name = input("What's ur name, playa? ")
	menu = Menu()
	# Counter-intuitive naming, I know. Short on time
	selected_option = menu.draw()
	if selected_option == "HS":
		controller = Controller(player_name)
		controller.initialize()
		input_map = parser_txt("rogue/levels/02")
		vs_main(input_map, controller)
	elif selected_option == "MAN":
		controller = Controller(player_name)
		controller.initialize()
		input_map = parser_txt("rogue/levels/02")
		vs_main(input_map, controller)
	elif selected_option == "P":
		controller = Controller(player_name)
		controller.initialize()
		input_map = parser_txt("rogue/levels/02")
		vs_main(input_map, controller)