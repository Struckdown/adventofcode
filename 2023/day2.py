def solve():
	f = open("input.txt", "r")
	sum = 0
	powerSum = 0

	limit = {"red":12, "green":13, "blue":14}

	for line in f:
		minimum = {"red":0, "green":0, "blue":0}
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
					#break	# we can't early break for part 2
				minimum[color] = max(minimum[color], count)

		# if valid, we can add to our sum
		if (valid):
			sum += gameNum

		# for part 2, we grab the cube power
		localPower = 1
		for color in minimum:
			localPower *= minimum[color]
		powerSum += localPower
		print(minimum, localPower)


	# output the answer
	print(sum)
	print(powerSum)

if __name__ == '__main__':
	solve()