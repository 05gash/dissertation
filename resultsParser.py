import re
import random
def resultsParse(location):
	results = [0,0,0,0,0]
	f = open(location, "r")
	for line in f:
		results[parseLine(line)] = results[parseLine(line)] + 1
	print results


def parseLine(line):
	rtn = ''
	line = line.replace(" ","")

	p = re.compile('sb|mb')

	o = re.compile('sw|mw')

	fields = line.split(',')
	first = fields[0].split('-')[0]
	second = fields[0].split('-')[1]
	if p.match(fields[1]): rtn = second
	elif o.match(fields[1]): rtn = first
	else: rtn = random.choice([first, second])	
	return int(rtn)


resultsParse('/home/ga354/Downloads/finals - Sheet1.csv')
resultsParse('/home/ga354/Downloads/finals - Sheet2.csv')
resultsParse('/home/ga354/Downloads/finals - Sheet3.csv')
