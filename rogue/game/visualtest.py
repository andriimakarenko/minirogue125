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
	message = controller.get_status()
	win.move(41 + ((height - 42) // 2), 0)
	win.clrtoeol()
	win.addstr(41 + ((height - 42) // 2), (width - 122) // 2, message)

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

def vs_draw_entities(input_map, controller, win, vshift, hshift):
	hero_y, hero_x = controller.get_hero_yx()
	win.addstr(hero_y + vshift, hero_x + hshift, "@")
	for item in controller.get_items():
		win.addstr(item[0] + vshift, item[1] + hshift, item[2])
	for enemy in controller.get_monsters():
		win.addstr(enemy[0] + vshift, enemy[1] + hshift, enemy[2])


def vs_main(input_map, controller):
	stdscr = curses.initscr()
	height, width = stdscr.getmaxyx()
	vert_shift = (height - 42) // 2
	hor_shift = (width - 122) // 2
	if height < 42 or width < 122:
		curses.endwin()
	curses.curs_set(0)
	curses.noecho()
	curses.cbreak()
	stdscr.keypad(True)
	while (controller.get_hero_hp() > 0):
		y, x = controller.get_hero_yx()
		vs_print_map(input_map, stdscr)
		vs_draw_entities(input_map, controller, stdscr, vert_shift, hor_shift)
		vs_print_stats_bar(controller, stdscr)
		key = stdscr.getch()
		if key == curses.KEY_UP:
			controller.try_move('u')
		elif key == curses.KEY_DOWN:
			controller.try_move('d')
		elif key == curses.KEY_LEFT:
			controller.try_move('l')
		elif key == curses.KEY_RIGHT:
			controller.try_move('r')
		elif key == curses.KEY_BACKSPACE or input_map[y][x] == '%':
			curses.curs_set(1)
			curses.echo()
			curses.nocbreak()
			stdscr.keypad(False)
			curses.endwin()
			break
		vs_print_message(controller.get_message(), stdscr)
	stdscr.getch()
	stdscr.erase()
	if controller.get_hero_hp() == -1337:
		stdscr.addstr(height // 2, width // 2 - 4, "CONGRATS!")
		msg = controller.get_final_count()
		stdscr.addstr(height // 2 + 1, width // 2 - (len(msg) // 2), msg)
		stdscr.getch()
	else:
		stdscr.addstr(height // 2, width // 2 - 8, "RIP and also -42")
		stdscr.getch()
	curses.curs_set(1)
	curses.echo()
	curses.nocbreak()
	stdscr.keypad(False)
	curses.endwin()