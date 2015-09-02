#Rock Beom Kim
#rk5dy
#Programming Assignment 4: Drainage
import sys

#open file and split into lines. Straightforward
f = open(sys.argv[1], "r")
fileLine = f.read()
f.close()
lines = fileLine.split("\n")

def findLPath(x, y, dp, m):
	surroundPoints = [a for a in [x-1, y], [x+1, y], [x, y+1], [x, y-1] if dp[a[0]][a[1]] < dp[x][y]]
	#base case: if there are no surrounding points, return 1
	if len(surroundPoints) == 0:
		return 1
	
	tmp = 0
	for a in surroundPoints:
		tmpL = 1
		#if there is an established path, just take it
		if (m[a[0]-1][a[1]-1] > 1):
			tmpL += m[a[0]-1][a[1]-1]
		#otherwise just go through the path brute force until an established path reached
		else:
			tmpL += findLPath(a[0], a[1], dp, m)
		#check for the best path, since not all established paths are equal
		if (tmp < tmpL):
			tmp = tmpL	
	return tmp

def findMax (rows, cols, dp):
	m = [[1 for x in range(0, cols)] for y in range(0, rows)]
	tmp = 1
	for x in range(1, rows + 1):
		for y in range(1, cols + 1):
			#iterates through the list of points and stores them in the 2d array m along the way
			m[x-1][y-1] = findLPath(x, y, dp, m)
			#take longest of the longest paths
			if (tmp < m[x-1][y-1]):
				tmp = m[x-1][y-1]
	return tmp
#number of cases is first line
noOfCases = int(lines[0])
indexOfCities = 1
while (noOfCases > 0):
	#each first line includes the city, rows and columns
	data = lines[indexOfCities].split(" ")
	noOfRows = int(data[1])
	noOfCols = int(data[2])
	
	#buffer the drainage points thing with sys.maxint as extra columns and rows to avoid worrying about bounds checking
	drainagePoints = []
	drainagePoints.append([sys.maxint for x in range(0, noOfCols + 2)])
	for i in range(1, noOfRows + 1):
		aRow = [sys.maxint]
		aRow.extend(lines[indexOfCities + i].split(" "))
		for a in range(1, noOfCols+1):
			aRow[a] = int(aRow[a])
		aRow.append(sys.maxint)
		drainagePoints.append(aRow)
	drainagePoints.append([sys.maxint for x in range(0, noOfCols + 2)])

	#output print
	a = findMax(noOfRows, noOfCols, drainagePoints)	
	print data[0].strip() + ": " + str(a)

	#terminate the loop
	noOfCases -= 1
	indexOfCities += noOfRows + 1
