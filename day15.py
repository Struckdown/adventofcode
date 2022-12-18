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

# Figure out how far to check along the row
rowBoundaries = [sensors[0].x, sensors[0].x]
for sensor in sensors:
	rowBoundaries[0] = min(rowBoundaries[0], sensor.x - sensor.range)
	rowBoundaries[1] = max(rowBoundaries[1], sensor.x + sensor.range)


count = 0
row = []
for x in range(rowBoundaries[0], rowBoundaries[1]+1):
	posToCheck = [x,2000000]
	row.append(".")
	for sensor in sensors:
		if sensor.canReach(posToCheck):
			if not (posToCheck in beacons):
				count += 1
				row[-1] = "#"
				break
#print(row)
print(count)