# Day 14
import math

world = []
startOffset = 400
for i in range(1000):
	row = []
	for j in range(1000):
		row.append(".")
	world.append(row)

def addRock(newRockPositions):
	global world
	newRockPositions = newRockPositions.replace("\n","")
	rocks = newRockPositions.split(" -> ")

	prevRock = rocks[0].split(",")
	for r in range(len(prevRock)):
		prevRock[r] = int(prevRock[r])
	first = True
	for rock in rocks:
		if first:
			first = False
			continue
		newRock = rock.split(",")
		for r in range(len(newRock)):
			newRock[r] = int(newRock[r])

		# see if new rock starting
		if prevRock[0] != newRock[0] and prevRock[1] != newRock[1]:
			prevRock = newRock
			continue

		# calculate line
		if prevRock[0] != newRock[0]:
			delta = newRock[0] - prevRock[0]
			dir = int(math.copysign(1,delta))	# evaluates to -1 or 1
			for i in range(prevRock[0], newRock[0] + dir, dir):
				world[i][prevRock[1]] = "#"
		if prevRock[1] != newRock[1]:
			delta = newRock[1] - prevRock[1]
			dir = int(math.copysign(1,delta))	# evaluates to -1 or 1
			for i in range(prevRock[1], newRock[1] + dir, dir):
				world[prevRock[0]][i] = "#"

		prevRock = newRock

def simulateSand():
	global world

	sandDropped = 0
	while True:

		curPos = (500, 0)
		hitMax = False
		while True:
			spacesToCheck = [(0, 1), (-1, 1), (1, 1)]
			freeSpace = False
			for space in spacesToCheck:
				newSpace = (curPos[0]+space[0],curPos[1]+space[1])
				if world[newSpace[0]][newSpace[1]] == ".":
					freeSpace = True
					break
			if not freeSpace:
				world[curPos[0]][curPos[1]] = "+"
				break
			curPos = newSpace
			if curPos[0] == 990 or curPos[1] == 990:
				hitMax = True
				break

		if hitMax:
			return sandDropped
		sandDropped += 1

def printWorld():
	global world
	for i in range(470, 530):
		for j in range(0, 11):
			print(world[i][j], end="")
		print()


with open('input.txt', 'r') as file:
	for line in file:
		addRock(line)

# TODO
# Simulate falling sand
#printWorld()
sand = simulateSand()
printWorld()
print(sand)
