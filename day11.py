# Day 11

class Monkey():
	def __init__(self):
		self.id = 0
		self.items = []
		self.operation = "*"
		self.testDivVal = 1
		self.monkeyA = -1
		self.monkeyB = -1

	def setup(self, id, startingItems, operation, testDivVal):
		self.id = id
		self.items = startingItems
		self.operation = operation
		self.testDivVal = int(testDivVal)
		self.inspectCount = 0

	def setMonkeys(self, A, B):
		self.monkeyA = A
		self.monkeyB = B

	def inspect(self):
		if len(self.items) <= 0:
			return
		item = self.items[0]
		item = int(eval(str(self.operation)))
		#item = int(item/3)	# Q1
		item %= 9699690		# Q2
		self.items[0] = item
		self.inspectCount += 1

	def throw(self):
		if len(self.items) <= 0:
			return
		targetMonkey = self.monkeyB
		item = self.items[0]
		if item % self.testDivVal == 0:
			targetMonkey = self.monkeyA

		targetMonkey.catch(item)
		self.items.pop(0)

	def catch(self, item):
		self.items.append(item)

	# Monkey does everything it wants to this round
	def activateMonkey(self):
		while len(self.items) > 0:
			self.inspect()
			self.throw()

	def printMonkey(self):
#		print("Items:"self.items)
		print("Monkey " + str(self.id) + ": Inspect Count: ", self.inspectCount)


def getMonkey(id):
	for monkey in monkeys:
		if monkey.id == id:
			return monkey
	return None

activeMonkey = None
monkeys = []
with open('input.txt', 'r') as file:
	id = -1
	items = []
	operation = None
	testDivVal = 1
	monkA = -1
	monkB = -1
	for line in file:
		if "Monkey" in line:
			activeMonkey = Monkey()
			id = int(line.replace(":","").split()[1])
		if "Starting" in line:
			items = line.replace(",","").split()[2:]
			for i in range(len(items)):
				items[i] = int(items[i])
		if "Operation" in line:
			operation = line.split("= ")[1]
			operation = operation.replace("old","item")
		if "Test" in line:
			testDivVal = int(line.split()[-1])
		if "true" in line:
			monkA = int(line.split()[-1])
		if "false" in line:
			monkB = int(line.split()[-1])
			activeMonkey.setup(id, items, operation, testDivVal)
			activeMonkey.setMonkeys(monkA, monkB)
			monkeys.append(activeMonkey)

# now that monkeys exist, replace their references to each other with proper monkeys
for monkey in monkeys:
	monkA = getMonkey(monkey.monkeyA)
	monkB = getMonkey(monkey.monkeyB)
	monkey.setMonkeys(monkA, monkB)

roundLimit = 10000
for i in range(1, roundLimit+1):
	for monkey in monkeys:
		monkey.activateMonkey()
	if i % 1000 == 0:
		print(i)
		for monkey in monkeys:
			monkey.printMonkey()
		print()

#for monkey in monkeys:
	#monkey.printMonkey()

