# Day 8

trees = []	# tree grid
totalVisibleTrees = []	# tree grid but 0s and 1s (1 if can be seen)

with open('input.txt', 'r') as file:

	# Init 2d array
	for line in file:
		arr = []
		arr2 = []
		for char in line:
			if char != "\n":
				arr.append(int(char))
				arr2.append(0)
		trees.append(arr)
		totalVisibleTrees.append(arr2)

# debug print grid
#for x in trees:
#	print(x)
#print()

for x in range(len(trees)):

	lowest = -1
	# left to right
	for y in range(len(trees[x])):
		if trees[x][y] > lowest:
			lowest = max(trees[x][y], lowest)
			totalVisibleTrees[x][y] = 1

	lowest = -1
	# right to left
	for y in range(len(trees[x])-1, -1, -1):
		if trees[x][y] > lowest:
			lowest = max(trees[x][y], lowest)
			totalVisibleTrees[x][y] = 1

	lowest = -1
	# top to bot # Assumes this is a perfect grid
	for y in range(len(trees[x])):
		if trees[y][x] > lowest:
			lowest = max(trees[y][x], lowest)
			totalVisibleTrees[y][x] = 1

	lowest = -1
	# bot to top 	# Assumes this is a perfect grid
	for y in range(len(trees[x])-1, -1, -1):
		if trees[y][x] > lowest:
			lowest = max(trees[y][x], lowest)
			totalVisibleTrees[y][x] = 1

count = 0
for x in totalVisibleTrees:
	count += sum(x)
print("Q1:", count)

# Q2
def getScore(treeY, treeX):
	visibleTrees = []
	height = trees[treeX][treeY]

	# looking left
	count = 0
	for x in range(treeX - 1, -1, -1):
		if trees[x][treeY] < height:
			count += 1
		else:
			count += 1
			break		# we stop if we find another tree of the same or greater height
	visibleTrees.append(count)

	# looking right
	count = 0
	for x in range(treeX + 1, len(trees[treeX])):
		if trees[x][treeY] < height:
			count += 1
		else:
			count += 1
			break
	visibleTrees.append(count)

	# looking up
	count = 0
	for y in range(treeY - 1, -1, -1):
		if trees[treeX][y] < height:
			count += 1
		else:
			count += 1
			break
	visibleTrees.append(count)

	# looking down
	count = 0
	for y in range(treeY + 1, len(trees[treeY])):
		otherTreeHeight = trees[treeX][y]
		if trees[treeX][y] < height:
			count += 1
		else:
			count += 1
			break
	visibleTrees.append(count)

	total = 1
	for i in visibleTrees:
		total *= i
	return total

# Calculate each score, only keep the best
bestScore = 0
for x in range(len(trees)):
	for y in range(len(trees[x])):
		score = getScore(y, x)
		bestScore = max(score,bestScore)
print("Q2:", bestScore)