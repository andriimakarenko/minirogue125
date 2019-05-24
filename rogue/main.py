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

def initialize_color_pairs():
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

# Curses documentation is shit tier, so for now I just draw the
# whole thing in the same main window. Later on I'll figure out
# how to use panels, cause that's what I need but that's what's
# documented the worst.

def work(stdscr):
	curses.curs_set(0)
	win_height, win_width = stdscr.getmaxyx()
	initialize_color_pairs()
	menu = Menu(win_height, win_width, stdscr)
	menu.draw()

def main():
	curses.wrapper(work)
