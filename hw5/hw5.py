#Rock Beom Kim
#rk5dy
#Programming Assignment 5: classes
import sys

#does edge exist?
def get_path(edges, sup_src, sup_sink):
	#loop through all classes student is enrolled in
	for stud in range(len(edges)):
		for a in range(len(edges[stud])):
			#residual = capacity - flow
			residual = edges[stud][a][0] - edges[stud][a][1]
			sink_resid = sup_sink[a][0] - sup_sink[a][1]
			src_resid = sup_src[stud][0] - sup_src[stud][1]
			
			#if residual > 0 and the edge is unvisited
			if residual > 0 and sink_resid > 0 and src_resid > 0 and edges[stud][a][3] == 0:
				'''	
				print "(" + str(stud) + ", " + str(a) + ")"
				print "residual of edge:  " + str(residual)
				print "residual of sink: " + str(sink_resid)
				print "residual of source: " + str(src_resid)
				'''
				return (stud, a)
				
				
	#if there is no edge, return -1
	return (-1, -1)

def try_other_e(edges, sup_src, sup_sink, a):
	#check classes of a to make sure there are other options available
	for b in range(len(edges[a])):
		#if stud-class edge unvisited and edge has nonzero capacity
		if edges[a][b][3] == 0 and edges[a][b][0] != 0:
			#find other students taking class
			for c in range(a):
				#if other edges leading to that class are not visited
				if edges[c][b][3] != 0:
					#find an alternative class for said student
					for d in range(len(edges[c])):
						#residuals
						residual = edges[c][d][0] - edges[c][d][1]
						sink_resid = sup_sink[d][0] - sup_sink[d][1]
						src_resid = sup_src[c][0] - sup_src[c][1]
						#print "Residual: " + str(residual) + " visited: " + str(edges[c][d][3])
						#if residuals check out well, then use that new class
						if edges[c][d][3] == 0 and residual > 0:
							#tuple has (student to be replaced, that student's new class, class of student with lacking class)`:w
							return (c, d, b)
	return (-1, -1, -1)

#edges = (capacity, flow, backflow, visited)
def ffulkerson(edges, sup_src, sup_sink):
	#foreach student
	#while there is path from class to student
	reqTuple = (0, 0)
	while (reqTuple[0] > -1):
		reqTuple = get_path(edges, sup_src, sup_sink)
		if reqTuple == (-1, -1):
			break
		stud_index = reqTuple[0]
		cls_index = reqTuple[1]
		'''
		normally I'd have to find min by going through the path, 
		but the nodes are individual students, 
		not varying # of students
		'''
		#mark edge as visited
		edges[stud_index][cls_index][3] = 1
		
		#add flow to each of the edges
		edges[stud_index][cls_index][1] += 1
		sup_src[stud_index][1] += 1
		sup_sink[cls_index][1] += 1

		#add backflow to each of the edges
		sup_src[stud_index][2] -= 1
		sup_src[stud_index][2] -= 1
		edges[stud_index][cls_index][1] -= 1
	finalCheck = 0
	for a in range(len(sup_src)):
		#if student has filled capacity, add to final check
		if sup_src[a][1] == sup_src[a][0]:
			finalCheck += sup_src[a][1]
		else:
			while (sup_src[a][1] != sup_src[a][0]):
				#tuple has (student to be replaced, that student's new class, class of student with lacking class)
				newTup = try_other_e(edges, sup_src, sup_sink, a)
				if (newTup[0] == -1):
					return -1
				prev_stud = newTup[0]
				prev_stud_cls = newTup[1]
				curr_stud_cls = newTup[2]

				#mark that edge as visited
				edges[prev_stud][prev_stud_cls][3] = 1
				edges[a][curr_stud_cls][3] = 1

				#update flow of current class
				edges[a][curr_stud_cls][1] += 1
				edges[a][curr_stud_cls][2] -= 1
				sup_src[a][1] += 1
				sup_src[a][2] -= 1
			finalCheck += sup_src[a][1]
	return finalCheck


#open file and split into lines. Straightforward
f = open(sys.argv[1], "r")
fileLine = f.read()
f.close()
lines = fileLine.split("\n")

#can be multiple requests
filei = 0
while (lines[filei] != "0 0 0"):
	#take three vals, create set of classes and set of students
	rcnvals = lines[filei].strip().split(" ")
	requests = []
	class_set = []
	stud_set = []
	
	#stud_set = [students]
	#requests = [(student, class)]
	for i in range(int(rcnvals[0])):
		curr_line = lines[i+1+filei].strip().split(" ")
		reqTuple = (curr_line[0], curr_line[1])
		requests.append(reqTuple)
		if (curr_line[0] not in stud_set):
			stud_set.append(curr_line[0])

	#class set with capacities
	#class_set = [("classname", capacity)]
	for i in range(int(rcnvals[1])):
		curr_line = lines[i+int(rcnvals[0])+1 + filei].strip().split(" ")
		class_set.append((curr_line[0], int(curr_line[1])))

	#edges = (capacity, flow, backflow, visited)
	edges = [[[0, 0, 0, 0] for a in class_set] for b in stud_set]
	#each student needs to take n classes
	supsource = [[int(rcnvals[2]), 0, 0, 0] for a in stud_set]
	#each class has a maximum value
	supsink = [[n, 0, 0, 0] for (a, n) in class_set]
	for a in range(len(stud_set)):
		for b in range(len(class_set)):
			this_class = class_set[b][0] 
			if (stud_set[a], this_class) in requests:
				edges[a][b][0] = 1
	
	result = ffulkerson(edges, supsource, supsink)
	#if result is not no_students * n, print no
	if result != (len(stud_set) * int(rcnvals[2])):
		print "No"
	else:
	#else print yes
		print "Yes"

	#file index = current + 1 + no_students + no_classes is incremented
	filei = filei + 1 + int(rcnvals[0]) + int(rcnvals[1]) 
