import re
import random
def resultsParse(location):
	results = [0,0,0,0,0]
	f = open(location, "r")
	for line in f:
		results[parseLine(line)] = results[parseLine(line)]+1
	print results


def parseLine(line):
	line = line.replace(" ","")

	p = re.compile('sb|mb')

	o = re.compile('sw|mw')

	fields = line.split(',')
	first = fields[0].split('-')[0]
	second = fields[0].split('-')[1]
	if p.match(fields[1]): return second
	elif o.match(fields[1]): return first
	else: return random.choice([first, second])	
