# Day 7

class Directory():

	def __init__(self):
		self.contents = []
		self.parent = None
		self.name = None

	# Recursively get size of directory and all children
	def getSize(self):
		sum = 0
		for i in self.contents:
			if type(i) == int:
				sum += i
			else:
				sum += i.getSize()
		return sum

	def getContents(self):
		return self.contents

	# Add item to directory
	def add(self, item):
		self.contents.append(item)

	# Each dir must point back to a parent
	def setParent(self, newParent):
		self.parent = newParent

	def getParent(self):
		return self.parent

	def setName(self, newName):
		self.name = newName

	def getName(self):
		return self.name

	def moveIntoDir(self, nameOfDir):
		if ".." == nameOfDir:
			return self.parent
		for child in self.contents:
			if type(child) != int:  # is a directory
				if child.getName() == nameOfDir:
					return child
		return

# Simulate the data using a dictionary
root = Directory()
curDir = root
command = None
with open('input.txt', 'r') as file:
	# Read "cd /"
	file.readline()
	while(True):
		curLine = file.readline()
		data = curLine.split()
		if "$" in curLine:
			curInstruction = curLine
			command = curInstruction.split()[1]
			if command == "ls":
				continue

		# Check to see if we exit
		if(curLine == ""):
			break

		# Act on current information
		if command == "ls":
			# Add data
			if data[0] == "dir":
				newDirectory = Directory()
				newDirectory.setParent(curDir)
				newDirectory.setName(data[1])
				curDir.add(newDirectory)	# add directory
			else:	# must not be a directory
				curDir.add(int(data[0]))	# add size, don't care about name of file, I think.

		if command == "cd":
			curDir = curDir.moveIntoDir(data[2])


dirUnderLimit = []
curDir = root
stack = []
allDirs = []
limit = 100000
while(True):
	for dir in curDir.getContents():
		if type(dir) != int:
			stack.append(dir)
			allDirs.append(dir)
			if (dir.getSize() < limit):
				dirUnderLimit.append(dir)
	if len(stack) == 0:
		break
	curDir = stack.pop()

total = 0
for dir in dirUnderLimit:
	total += dir.getSize()
print(total)


# Q2
MAX_MEMORY = 70000000
DESIRED_FREE_MEMORY = 30000000
USED_MEMORY = root.getSize()
FREE_MEMORY = MAX_MEMORY - USED_MEMORY
MEMORY_TO_CLEAR_MINIMUM = DESIRED_FREE_MEMORY - FREE_MEMORY

SizesOfDir = []
for dir in allDirs:
	if dir.getSize() >= MEMORY_TO_CLEAR_MINIMUM:
		SizesOfDir.append(dir.getSize())
SizesOfDir.sort()
print(SizesOfDir[0])
