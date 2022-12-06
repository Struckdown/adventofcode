# Day 5


stacks = []
height = 0
with open('input.txt', 'r') as file:
	for line in file:
		totalStacks = int(len(line)/4)
		file.seek(0)
		break
	for _ in range(totalStacks):
		stacks.append([])		# set up empty stacks


	# Fill stacks representation
	for line in file:
		i = 0
		if "[" in line:
			for char in line:
				stack = int(i/4)
				if char not in "[]\n\\ ":
					stacks[stack].append(char)		# "[X] " is 4 chars
				i += 1
			height += 1


	file.seek(0)

	# perform moves
	for line in file:
		symbols = line.split(" ")
		if symbols[0] != "move":
			continue
		stackToPull = int(symbols[3])-1
		stackToGive = int(symbols[5])-1
		movesToMake = int(symbols[1])

		#Q1 moves
		#for symbol in range(movesToMake):
		#	val = stacks[stackToPull].pop(0)
		#	stacks[stackToGive].insert(0, val)

		#Q2 moves
		curBoxes = []
		for symbol in range(movesToMake):
			box = stacks[stackToPull].pop(0)
			curBoxes.append(box)
		curBoxes.reverse()
		for box in curBoxes:
			stacks[stackToGive].insert(0, box)


for s in stacks:
	print(s[0], end="")

