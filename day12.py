# Day 12
import queue

class Grid():
	def __init__(self, grid, depthGrid):
		self.grid = grid
		self.depthGrid = depthGrid

	def canTravel(self, curPos, destination):
		# Check for OOB
		if curPos[0] < 0 or destination[0] < 0:
			return False
		if curPos[0] >= len(self.grid) or destination[0] >= len(self.grid):
			return False
		if curPos[1] < 0 or destination[1] < 0:
			return False
		if curPos[1] >= len(self.grid[0]) or destination[1] >= len(self.grid[0]):
			return False

		# Check to see if valid letter for exploring
		curPosLetter = self.grid[curPos[0]][curPos[1]].lower()
		desPosLetter = self.grid[destination[0]][destination[1]].lower()

		if ord(curPosLetter) + 1 < (ord(desPosLetter)):			# can only travel if new position has valid letter
			return False

		# check if can explore
		curDepth = self.depthGrid[curPos[0]][curPos[1]]
		destinationDepth = self.depthGrid[destination[0]][destination[1]]
		if destinationDepth == 0:		# unexplored is always valid
			return True
		if curDepth >= destinationDepth:		# never explore another path that is more efficient
			return False

		return True

	def print(self):
		for row in range(len(self.grid)):
			for column in range(len(self.grid[row])):
				print(self.depthGrid[row][column], sep="", end="    ")
			print()
		print()

	def solve(self, startingPos):
		q = queue.SimpleQueue()

		curPos = startingPos
		q.put(curPos)		# add first pos

		while q.qsize() > 0:
			curPos = q.get()
			curLetter = self.grid[curPos[0]][curPos[1]]
			curDepth = self.depthGrid[curPos[0]][curPos[1]]

			# try to move in all directions
			directions = [(-1,0), (1,0), (0,-1), (0,1)]
			for dir in directions:
				newPos = (curPos[0] + dir[0], curPos[1] + dir[1])
				try:
					newLetter = self.grid[newPos[0]][newPos[1]]
				except:
					newLetter = "b"
				if self.canTravel(curPos, newPos):
					newPosPrevDepth = self.depthGrid[newPos[0]][newPos[1]]
					prevDepth = 9999 if newPosPrevDepth == 0 else newPosPrevDepth
					newDepthIsLower = curDepth + 1 < prevDepth
					self.depthGrid[newPos[0]][newPos[1]] = min(curDepth + 1, prevDepth)
					if newLetter == "a":
						self.depthGrid[newPos[0]][newPos[1]] = 1		# override with 1 if it's 'a'
					if newDepthIsLower:
						q.put(newPos)
		return self.depthGrid[curPos[0]][curPos[1]]

grid = []
depthGrid = []
startPos = (0,0)
destinationPosition = (0,0)
row = 0; column = 0
with open('input.txt', 'r') as file:
	for line in file:
		column = 0
		arr = []
		depthArr = []
		for char in line:
			if char == "\n":
				continue
			if char == "S":
				arr.append("a")
				startPos = (row, column)
			elif char == "E":
				arr.append("{")
				destinationPosition = (row, column)
			else:
				arr.append(char)
			depthArr.append(0)
			column += 1
		row += 1
		grid.append(arr)
		depthGrid.append(depthArr)

print(len(grid), len(grid[0]))

Grid = Grid(grid, depthGrid)
Grid.solve(startPos)

ans = Grid.depthGrid[destinationPosition[0]][destinationPosition[1]] - 1
print(ans)