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
from rogue.game.controller import Controller

def vs_print_stats_bar(controller, win):
	height, width = win.getmaxyx()
	win.move(41 + ((height - 42) // 2), 0)
	win.clrtoeol()
	#to do print stats bar

def vs_print_message(msg, win):
	win.move(1, 0)
	win.clrtoeol()
	win.addstr(1, 0, msg)
	win.refresh

def vs_print_map(input_map, win):
	height, width = win.getmaxyx()
	vert_shift = (height - 42) // 2
	hor_shift = (width - 122) // 2
	y = 0
	while y < len(input_map):
		x = 0
		while x < len(input_map[y]):
			if True:
				if input_map[y][x] == '+':
					win.addstr(y + vert_shift, x + hor_shift, "█")
				elif input_map[y][x] == '#':
					win.addstr(y + vert_shift, x + hor_shift, "░")
				else:
					win.addstr(y + vert_shift, x + hor_shift, input_map[y][x])
			x += 1
		y += 1

def vs_draw_entities(input_map, controller, win):
	hero_y, hero_x = controller.get_hero_yx()
	# win.attron(A_BOLD)
	win.addstr(hero_y + vert_shift, hero_x + hor_shift, "@")
	for item in controller.get_items():
		win.addstr(item[0] + vert_shift, item[1] + hor_shift, item[2])
	for enemy in controller.get_monsters():
		win.addstr(enemy[0] + vert_shift, enemy[1] + hor_shift, enemy[2])


def vs_main(input_map, controller):
	stdscr = curses.initscr()
	# curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
	# curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
	# curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
	# curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
	height, width = stdscr.getmaxyx()
	vert_shift = (height - 42) // 2
	hor_shift = (width - 122) // 2
	#if height < 42 or width < 122
		#term size is too small
	# win = curses.newwin(42, 122, (height - 42) // 2, (width - 122) // 2)
	curses.curs_set(0)
	curses.noecho()
	curses.cbreak()
	stdscr.keypad(True)
	vs_print_map(input_map, stdscr)
	# vs_print_stats_bar(controller, stdscr)
	while (controller.get_hero_hp() > 0):
		# vs_draw_entities(input_map, controller, stdscr)
		y, x = controller.get_hero_yx()
		stdscr.addstr(y + vert_shift, x + hor_shift, "@")
		key = stdscr.getch()
		if key == curses.KEY_UP:
			controller.try_move('u')
		elif key == curses.KEY_DOWN:
			controller.try_move('d')
		elif key == curses.KEY_LEFT:
			controller.try_move('l')
		elif key == curses.KEY_RIGHT:
			controller.try_move('r')
		#elif key == 'q'
			#exit and show menu;
	curses.curs_set(1)
	curses.echo()
	curses.nocbreak()
	stdscr.keypad(False)
	curses.endwin()

# def draw_game():
# 	curses.wrapper(main)