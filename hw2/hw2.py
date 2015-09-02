#Rock Beom Kim
#rk5dy
#Programming Assignment 2: Moving
import sys
lines = sys.__stdin__.readlines()

def tupleComp(a, b):
	if a[1] == b[1]:
		return cmp(a[0],b[0])
	else:
		return cmp(a[1],b[1])

noOfCases = int(lines[0])
lineCount = 1
caseC = 1
for a in range(0, noOfCases):
	firstLine = lines[lineCount].split(" ")
	totBoxes = int(firstLine[0])
	toTake = int(firstLine[1])
	companyC = int(firstLine[2])
	caseNum = "Case " + str(caseC)
	#print str(noOfBoxes)
	companies = []
	for b in range(0, companyC):
		companyD = lines[lineCount + 1 + b].split(" ")
		cName = companyD[0].strip()
		cfs = int(companyD[1])
		css = int(companyD[2])
		tmpBoxes = totBoxes
		cost = 0
		while ((tmpBoxes/2) > toTake and css/(tmpBoxes - toTake) < cfs):
			tmpBoxes /= 2
			cost += css
		cost += (tmpBoxes - toTake) * cfs
		companies.append((cName, cost))
	companies.sort(cmp = tupleComp)
	lineCount += companyC + 1
	print caseNum
	for a in companies:
		print a[0] + " " + str(a[1])
	caseC += 1
	#print str(noOfBoxes) + " " + str(noNeedToShip) + " " + str(companies)
