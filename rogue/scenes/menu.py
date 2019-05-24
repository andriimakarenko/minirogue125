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
from rogue.game.visual import start_game

class Menu(object):
	def __init__(self, height, width, window):
		self.options = ["Play", "Highscore", "Manual", "Quit"]
		self.switcher = {0: start_game,
										1: self.print_highscore, 2: self.print_manual}
		self.height = height
		self.width = width
		self.window = window

	def __repr__(self):
		return "Later"

# Maybe print_menu() and draw() should be class methods,
# not instance methods?

	def print_menu(self, selected):
		self.window.clear()
		for idx, option in enumerate(self.options):
			x = self.width // 2 - len(option) // 2
			y = self.height // 2 - len(self.options) // 2 + idx
			if idx == selected:
				self.window.attron(curses.color_pair(1))
				self.window.addstr(y, x, option)
				self.window.attroff(curses.color_pair(1))
			else:
				self.window.addstr(y, x, option)
			self.window.refresh()

"""
Mind you, the path to highscores is relative to the cwd at the moment
of the script launch. Won't work if cwd is different
from where start.py is
"""
	def print_highscore(self, window):
		try:
			with open("rogue/highscores.csv", 'r', newline='') as highscores_csv:
				highscores_reader = csv.DictReader(highscores_csv, delimiter='@')
			window.addstr(10, 10, "Well, it does work")
			window.refresh()
				# Should output dictionary entries from highscores_reader
				# to the center, 1 by 1 in the order by score
		except IOError:
			window.addstr(10, 10, "Well, it didon't work")

	def print_manual(self, window):
		pass

	def draw(self):
		self.window.clear()
		self.selected = 0
		self.print_menu(self.selected)

		while True:
			key = self.window.getch()

			if key == curses.KEY_UP and self.selected > 0:
				self.selected -= 1
				self.print_menu(self.selected)
			if key == curses.KEY_DOWN and self.selected < len(self.options) - 1:
				self.selected += 1
				self.print_menu(self.selected)
			if key == curses.KEY_ENTER or key in [10, 13]:
				self.window.clear()
				if self.selected == len(self.options) - 1:
					break
				self.switcher[self.selected](self.window)