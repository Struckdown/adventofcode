# Day 2

# Given a string, find a shared letter between the two halves
def findSharedLetter(input):
	count = len(input)
	half = int(count/2)
	for l in input[:half]:
		if l in input[half:]:
			return l

# input is an array of 3 elements of strings
def findSharedLetterInTripleLine(input):
	for l in input[0]:
		if l in input[1] and l in input[2]:
			return l

# converts a letter to 1-26 if lower case, 27-52 if uppercase
def convertLetterToValue(input):
	val = ord(input) - 96
	if val <= 0:	# must be upper case
		return ord(input) - 64 + 26
	return val

count = 0
count2 = 0
with open('input.txt', 'r') as file:

	activeLines = []
	for line in file:

		# puz 1
		sharedLetter = findSharedLetter(line)
		val = convertLetterToValue(sharedLetter)
		count += val

		# puz 2
		activeLines.append(line)
		if len(activeLines) == 3:
			letter = findSharedLetterInTripleLine(activeLines)
			count2 += convertLetterToValue(letter)
			activeLines.clear()

print(count)
print(count2)