# Day 2

# Given two letters, return win or loss
# 0 for loss, 3 for tie, 6 for win
def determineWinner(a, b):
	if a == "A" and b == "Y":
		return 6
	if a == "B" and b == "Z":
		return 6
	if a == "C" and b == "X":
		return 6
	if areSame(a, b):
		return 3
	return 0

# determine desired outcome
# a is opponent's symbol, b is desired outcome
# Returns symbol for you to get the desired outcome
def getDesiredSymbol(a, b):
	row = convertLetterToScore(a) - 1
	column = convertLetterToScore(b) - 1

	# Loss, tie, Win
	outcome =\
		[["Z", "X", "Y"],	# rock (for opponent)
	 	["X", "Y", "Z"],	# paper
		["Y", "Z", "X"]	# scissors
	 ]
	return outcome[row][column]

# Returns if the two inputs are the same or not
def areSame(a, b):
	if a == "A" and b == "X":
		return True
	if a == "B" and b == "Y":
		return True
	if a == "C" and b == "Z":
		return True
	return False

def convertLetterToScore(l):
	if l == "X" or l == "A":
		return 1
	if l == "Y" or l == "B":
		return 2
	if l == "Z" or l == "C":
		return 3

puzzle1score = 0
puzzle2score = 0
with open('input.txt', 'r') as file:
	for line in file:
		choices = line.split()
		a = choices[0]
		b = choices[1]

		# Puzzle 1
		roundScore = determineWinner(a,b)
		choiceScore = convertLetterToScore(b)
		puzzle1score = puzzle1score + roundScore + choiceScore

		# Puzzle 2
		c = getDesiredSymbol(a, b)
		roundScore = determineWinner(a,c)
		choiceScore = convertLetterToScore(c)
		puzzle2score = puzzle2score + roundScore + choiceScore

print(puzzle1score)
print(puzzle2score)
