# Day 15

sensors = []
beacons = []

class Sensor():
	def __init__(self, x, y):
		self.range = 0
		self.x = x
		self.y = y

	# pos is (x,y) coords
	def getDist(self, pos):
		dist = 0
		dist += abs(self.x - pos[0])
		dist += abs(self.y - pos[1])
		return dist

	def canReach(self, pos):
		return self.getDist(pos) <= self.range

	# row is the y coordinate
	def getRangeForRow(self, row):
		if not self.canReach([self.x,row]):
			return None
		remainingDist = abs(abs((self.y - row)) - self.range)
		return range(self.x-remainingDist,self.x+remainingDist+1)

def rangeOverlap(a,b):
	# check if b in a
	if a[0] >= b[0] and a[0] <= b[-1]+1:
		return True
	if a[-1]+1 >= b[0] and a[-1]+1 <= b[-1]+1:
		return True

	# check if a in b
	if b[0] >= a[0] and b[0] <= a[-1]+1:
		return True
	if b[-1]+1 >= a[0] and b[-1]+1 <= a[-1]+1:
		return True

	return False

def mergeRange(a, b):
		x = min(a[0],b[0])
		y = max(a[-1]+1,b[-1]+1)
		return range(x,y)

def attemptMerge(ranges, inputIndex):
	ranges = sorted(ranges, key=lambda r: r.start)
	newRanges = ranges

	while True:
		mergePerformed = False
		if len(ranges) == 1:
			return ranges

		newRanges = []

		for i in range(0, len(ranges)):
			if i == inputIndex:
				continue
			try:
				if rangeOverlap(ranges[inputIndex], ranges[i]):
					ranges[inputIndex] = mergeRange(ranges[inputIndex], ranges[i])
					mergePerformed = True
				else:
					newRanges.append(ranges[i])
			except:
				break

		if mergePerformed:
			newRanges.insert(0, ranges[inputIndex])
			ranges = newRanges.copy()

		if not mergePerformed:
			break
	return ranges

# Given a list of ranges, returns all merges as condensed as possible
def attemptMerges(ranges):
	j = 0
	ranges = sorted(ranges, key=lambda r: r.start)
	while True:
		if j >= len(ranges):
			break

		beforeMergeCount = len(ranges)
		ranges = attemptMerge(ranges, j)
		if beforeMergeCount == len(ranges):
			break
		j += 1
	return ranges

with open('input.txt', 'r') as file:
	for line in file:
		frags = line.replace(",","").replace(":","").split()
		x = int(frags[2][2:])
		y = int(frags[3][2:])
		sensor = Sensor(x,y)

		# beacon stats
		x = int(frags[8][2:])
		y = int(frags[9][2:])
		beacons.append([x,y])
		sensor.range = sensor.getDist((x,y))

		sensors.append(sensor)

# # Figure out how far to check along the row
# rowBoundaries = [sensors[0].x, sensors[0].x]
# for sensor in sensors:
# 	rowBoundaries[0] = max(0, min(rowBoundaries[0], sensor.x - sensor.range))
# 	rowBoundaries[1] = min(4000000, max(rowBoundaries[1], sensor.x + sensor.range))
#
#
# count = 0
#row = []

# Part 1
# for x in range(rowBoundaries[0], rowBoundaries[1]+1):
# 	print(x)
# 	for y in range(0, 4000000):
# 		posToCheck = [x,y]
# 		#row.append(".")
# 		canAnyReach = False
# 		for sensor in sensors:
# 			if sensor.canReach(posToCheck):
# 				canAnyReach = True
# 				break
# 		if not canAnyReach:
# 			print(posToCheck)
# 			print(posToCheck[0]*4000000+posToCheck[1])
# 			exit()
# 				# if not (posToCheck in beacons):
# 				# 	count += 1
# 				# 	row[-1] = "#"
# 				# 	break
#print(row)

# part 2

#for row in range(0, 20):
for row in range(2600000, 2700000):
	if row % 100000 == 0:
		print(row)
	ranges = []
	for sensor in sensors:
		newRange = sensor.getRangeForRow(row)
		if newRange != None:
			ranges.append(newRange)
	merged = attemptMerges(ranges)
	if len(merged) > 1:
		merged = sorted(merged, key=lambda r: r.start)
		print(row, merged)
		print((4000000*(merged[0][-1]+1))+row)


a = range(-8,12)
b = range(12,26)
c = rangeOverlap(a,b)
print(c)