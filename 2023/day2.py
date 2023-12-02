def solve():
	f = open("input.txt", "r")
	sum = 0

	limit = {"red":12, "green":13, "blue":14}

	for line in f:
		gameNum = line.split(":")[0].split()[1]
		gameNum = int(gameNum)
		cubes = line.split(":")[1]
		valid = True

		for cubeSet in cubes.split(";"):
			# cubeSet is x red, y green, z blue (and not all 3 are guaranteed to be there)
			currentSet = {}
			cubes = cubeSet.split(",")
			for cube in cubes:
				count = int(cube.split()[0])
				color = cube.split()[1]
				currentSet[color] = count
				if count > limit[color]:
					valid = False
					break

		# if valid, we can add to our sum
		if (valid):
			sum += gameNum


	# output the answer
	print(sum)

if __name__ == '__main__':
	solve()