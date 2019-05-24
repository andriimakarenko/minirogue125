import csv

try:
	with open("../highscores.csv", 'r', newline='') as highscores_csv:
		highscores_reader = csv.DictReader(highscores_csv, delimiter='@')
		print("Open OK")
except IOError:
	pass
