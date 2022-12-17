# Day 13

def isSorted(lhs, rhs):
	#print()
	#print(lhs)
	#print(rhs)

	# both inputs are int
	if type(lhs) == int and type(rhs) == int:
		if lhs > rhs:
			return -1
		if lhs < rhs:
			return 1
		if lhs == rhs:
			return 0

	# inputs are not the same type
	# convert both to lists
	if type(lhs) != type(rhs):
		if type(lhs) == int:
			lhs = [lhs]
		if type(rhs) == int:
			rhs = [rhs]

		subset = isSorted(lhs, rhs)
		return subset

	# both inputs are lists
	if type(lhs) == list and type(rhs) == list:
		for i in range(max(len(lhs),len(rhs))):
			try:
				l = lhs[i]
			except:
				return 1
			try:
				r = rhs[i]
			except:
				return -1

			subset = isSorted(l, r)
			if subset != 0:
				return subset

	return 0


sortedIndicies = []
sortedList = []
sortedList.append([[2]])
sortedList.append([[6]])

with open('input.txt', 'r') as file:
	i = 0
	j = 1
	for line in file:

		#Q2
		for i in range(len(sortedList)):
			if line == "\n":
				continue
			newElement = eval(line)
			ele = sortedList[i]
			inOrder = isSorted(ele, newElement)
			if inOrder == -1:
				sortedList.insert(i, newElement)
				break

		# #Q1
		# if i % 3 == 0:
		# 	left = eval(line)
		# if i % 3 == 1:
		# 	right = eval(line)
		# if i % 3 == 2:
		# 	sorted = isSorted(left, right)
		# 	if sorted >= 0:
		# 		sorted = True
		# 	else:
		# 		sorted = False
		# 	print(sorted)
		# 	if sorted:
		# 		sortedIndicies.append(j)
		# 	j += 1
		# i += 1

print("Sorted: ", sortedIndicies)
print(sum(sortedIndicies))

indicies = []
for i in range(len(sortedList)):
	print(sortedList[i])
for i in range(len(sortedList)):
	if sortedList[i] == [[2]] or sortedList[i] == [[6]]:
		print(i+1)
		indicies.append(i+1)

total = 1
for ele in indicies:
	total *= ele
print(total)