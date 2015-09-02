#Rock Beom Kim
#rk5dy
#Programming Assignment 1: Change
import sys           
lines = sys.__stdin__.readlines() 

for a in lines:
	intermediate = a.split(".")[0]
	if (float(intermediate) >= 0):
		tmp = ""
		temp = float(a.split(".")[1])
		while (temp > 0):
			if temp >= 25:
				tmp += "Q "
				temp -= 25
			elif temp >= 10:
				tmp += "D "
				temp -= 10
			elif temp >= 5:
				tmp += "N "
				temp -= 5
			else:
				tmp += "P "
				temp -= 1
		
		dollars = ""
		tempS = str(int(a.split(".")[1]))
		tempI = int(a.split(".")[1])
		while (len(intermediate) > 3):
			dollars = "," + intermediate[-3:] + dollars
			intermediate = intermediate[:-3]
		finalL = ""
		
		if tempI < 10:
			tempS = "0" + tempS
		
		finalL = "$" + intermediate + dollars + "." + tempS + " " + tmp
		
		print finalL
	else:
		break