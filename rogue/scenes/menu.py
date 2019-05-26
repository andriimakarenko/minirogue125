#####################################################################
#     ____       ____  _________    ____  ____  __________________  #
#    / __ \_  __/ __ \/ ____/   |  / __ \/ __ )/ ____/ ____/ ____/  #
#   / / / / |/_/ / / / __/ / /| | / / / / __  / __/ / __/ / /       #
#  / /_/ />  </ /_/ / /___/ ___ |/ /_/ / /_/ / /___/ /___/ __/      #
#  \____/_/|_/_____/_____/_/  |_/_____/_____/_____/_____/_/         #
#                                                                   #
#####################################################################

import curses
import csv

# def initialize_color_pairs():
	# curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

class Menu(object):
	def __init__(self):
		self.options = ["Play", "Highscore", "Manual", "Quit"]
		self.switcher = {0: "P", 1: "HS", 2: "MAN", 3: "Q"}
		self.height = 0
		self.width = 0

	def __repr__(self):
		return "Later"

	# All the below methods should prolly be class, not instance methods

	def print_menu(self, selected, stdscr):
		stdscr.clear()
		for idx, option in enumerate(self.options):
			x = self.width // 2 - len(option) // 2
			y = self.height // 2 - len(self.options) // 2 + idx
			if idx == selected:
				# stdscr.attron(curses.color_pair(1))
				stdscr.addstr(y, x - 5, " --> " + option + " <-- ")
				# stdscr.attroff(curses.color_pair(1))
			else:
				stdscr.addstr(y, x, option)
			stdscr.refresh()

	# TODO: decorate it, decorator calls a wrapper on it
	#	@wrap_it
	def print_highscore(self, stdscr):
		try:
			with open("rogue/highscores.csv", 'r', newline='') as highscores_csv:
				highscores_reader = csv.DictReader(highscores_csv, delimiter='@')
			stdscr.addstr(10, 10, "Well, it does work")
			stdscr.refresh()
				# Should output dictionary entries from highscores_reader
				# to the center, 1 by 1 in the order by score
		except IOError:
			stdscr.addstr(10, 10, "Well, it didon't work")
		stdscr.getch() # Wait's for any key to be pressed before closing

	# @wrap_it
	def print_manual(self, stdscr):
		pass

	# @wrap_it
	def draw(self, stdscr = None):
		stdscr = curses.initscr()
		curses.curs_set(0)
		curses.noecho()
		curses.cbreak()
		stdscr.keypad(True)

		self.height, self.width = stdscr.getmaxyx()
		# initialize_color_pairs()
		self.selected = 0
		self.print_menu(self.selected, stdscr)

		while True:
			key = stdscr.getch()

			if key == curses.KEY_UP and self.selected > 0:
				self.selected -= 1
				self.print_menu(self.selected, stdscr)
			if key == curses.KEY_DOWN and self.selected < len(self.options) - 1:
				self.selected += 1
				self.print_menu(self.selected, stdscr)
			if key == curses.KEY_ENTER or key in [10, 13]:
				curses.curs_set(1)
				curses.echo()
				curses.nocbreak()
				stdscr.keypad(False)
				curses.endwin()
				
				return self.switcher[self.selected]