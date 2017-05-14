import re
import random
import numpy

def resultsParse(location):
	n = 4
	MM = numpy.zeros(shape=(10, n*n))
	results = numpy.matrix('0,0,0,0; 0,0,0,0;0,0,0,0;0,0,0,0')
	f = open(location, "r")
	
	lineCounter = 0; #line counter
	observerMat = numpy.zeros(shape=(n,n))
	for line in f:
		if (lineCounter % 6 == 5):
			MM[lineCounter/6] = observerMat.flatten()
			observerMat = numpy.zeros(shape=(n,n))
		
		(i,j, amount) = parseLine(line)
		
		for mat in [observerMat, results]:
			mat[i,j] = mat[i,j] + amount
			mat[j,i] = mat[j,i] + (3 - amount)
		
		lineCounter = lineCounter + 1
	print "Results Matrix for " + location
	print results
	print "MM Matrix for same location"
	print MM
	f.close()

def parseLine(line):
	rtn = ''
	line = line.replace(" ","")

	p = re.compile('sb|mb')

	o = re.compile('sw|mw')
	
	amt = re.compile('mw|mb')



	fields = line.split(',')
	first = fields[0].split('-')[0]
	second = fields[0].split('-')[1]
	amount = 3 if amt.match(fields[1]) else 2

	if p.match(fields[1]): rtn = (second, first)
	elif o.match(fields[1]): rtn = (first, second)
	else: rtn = random.choice([(first, second), (second,first)])	
	return (int(rtn[0]) - 1, int(rtn[1]) - 1, amount)


resultsParse('/home/ga354/finals - Sheet1.csv')
resultsParse('/home/ga354/finals - Sheet2.csv')
resultsParse('/home/ga354/finals - Sheet3.csv')
