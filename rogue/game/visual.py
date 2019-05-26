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

def vs_print_stats_bar(controller, win):
	win.move(41, 0)
	win.clrtoeol()
	#to do print stats bar

def vs_print_message(msg, win):
	win.move(1, 0)
	win.clrtoeol()
	win.addstr(1, 0, msg)
	win.refresh

def vs_print_map(input_map, win, controller):
	y = 0
	while y < len(input_map):
		x = 0
		while x < len(input_map[y]):
			if controller.is_lighted(y, x):
				if input_map[y][x] == '+':
					win.addstr(y, x, "█")
				elif input_map[y][x] == '#':
					win.addstr(y, x, "░")
				else:
					win.addstr(y, x, input_map[y][x])
			x += 1
		y += 1

def vs_draw_level(input_map, controller, win):
	vs_print_map(input_map, win, controller)
	hero_y, hero_x = controller.get_hero_yx()
	# win.attron(A_BOLD)
	win.addstr(hero_y, hero_x, "@")
	for item in controller.get_items():
		win.addstr(item[0], item[1], item[2])
	for enemy in controller.get_monsters():
		win.addstr(enemy[0], enemy[1], enemy[2])


def vs_main(input_map, controller):
	stdscr = curses.initscr()
	# curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
	# curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
	# curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
	# curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
	height, width = stdscr.getmaxyx()
	#if height < 42 or width < 122
		#term size is too small
	win = curses.newwin(42, 122, (height - 42) // 2, (width - 122) // 2)
	curses.curs_set(0)
	curses.noecho()
	curses.cbreak()
	win.keypad(True)
	vs_draw_level(input_map, controller, win)
	vs_print_stats_bar(controller, win)
	while (controller.get_hero_hp() > 0):
		key = win.getch()
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
		vs_draw_level(input_map, controller, win)
	curses.curs_set(1)
	curses.echo()
	curses.nocbreak()
	win.keypad(False)
	curses.endwin()

# def draw_game():
# 	curses.wrapper(main)