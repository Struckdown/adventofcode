# Day 9

# Knots are basically a linked list
class Knot():
	def __init__(self):
		self.pos = [0,0]
		self.child = None
		self.parent = None
		self.id = 1
		self.visitedPos = [[0,0]]

	def propogateMovement(self, newPosition):
		if self.parent == None:
			self.pos = newPosition
			self.child.propogateMovement(self.pos)
		else:
			if movesToMatch(self.pos, self.parent.pos) >= 2:
				bestMove = self.getBestMove()
				self.pos[0] += bestMove[0]
				self.pos[1] += bestMove[1]

				if self.id == 10:
					if not(self.pos.copy() in self.visitedPos):
						self.visitedPos.append(self.pos.copy())

				if self.child:
					self.child.propogateMovement(self.pos)


	def addKnot(self, newKnot):
		self.child = newKnot
		self.child.id = self.id + 1
		self.child.parent = self

	def getChild(self, id):
		if self.id == id:
			return self
		return self.child.getChild(id)

	def getBestMove(self):
		ppos = self.parent.pos
		myPos = self.pos

		# no move needed
		if movesToMatch(ppos, myPos) <= 1:
			return [0,0]

		bestMove = [0,0]
		if (ppos[0] == myPos[0] or ppos[1] == myPos[1]):
			if ppos[0] == myPos[0]:
				if ppos[1] - myPos[1] > 0:
					bestMove[1] = 1
				else:
					bestMove[1] = -1
				return bestMove
			else:
				if ppos[0] - myPos[0] > 0:
					bestMove[0] = 1
				else:
					bestMove[0] = -1
				return bestMove

		if ppos[0] > myPos[0]:
			bestMove[0] = 1
		else:
			bestMove[0] = -1
		if ppos[1] > myPos[1]:
			bestMove[1] = 1
		else:
			bestMove[1] = -1
		return bestMove




ropeHead = Knot()
curKnot = ropeHead
ROPELENGTH = 10		# knots, including head
for i in range(ROPELENGTH-1):
	newKnot = Knot()
	curKnot.addKnot(newKnot)
	curKnot = newKnot

# return moves need to get between 2 vec, allowing for digaonal movements
def movesToMatch(a, b):
	delta = a[0] - b[0], a[1]-b[1]
	return max(abs(delta[0]), abs(delta[1]))

def diff(v1, v2):
	delta = a[0] - b[0], a[1]-b[1]
	return delta

def move(dir, distance):
	for i in range(distance):
		# Move head
		newPos = ropeHead.pos
		if dir == "U":
			newPos[1] += 1
		if dir == "R":
			newPos[0] += 1
		if dir == "D":
			newPos[1] -= 1
		if dir == "L":
			newPos[0] -= 1
		ropeHead.propogateMovement(newPos)

with open('input.txt', 'r') as file:
	for line in file:
		data = line.split()
		dir = data[0]
		distance = int(data[1])
		move(dir,distance)

tail = ropeHead.getChild(10)
print(len(tail.visitedPos))