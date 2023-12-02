def solve():
	f = open("input.txt", "r")
	sum = 0
	for line in f:
		firstNum = -1
		secondNum = -1
		for char in line:
			if char.isdigit():
				if (firstNum == -1):
					firstNum = int(char)
				secondNum = int(char)

		sum += int(str(firstNum) + str(secondNum))

	print(sum)

if __name__ == '__main__':
	solve()