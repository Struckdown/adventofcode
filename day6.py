# Day 6

# Takes in an array of size 4, returns true if no matches
def checkForMatches(input):
	anyMatches = False
	k = 0
	for c in input:
		j = 0
		for d in input:
			if k != j and c == d:
				anyMatches = True
			j += 1
		k += 1
	return anyMatches


with open('input.txt', 'r') as file:
	for line in file:
		i = 0
		recentChars = []
		for char in line:
			i += 1
			recentChars.append(char)
			if len(recentChars) > 14:		# replace with 4 for Q1
				recentChars.pop(0)
			else:
				continue
			matches = checkForMatches(recentChars)
			if not matches:
				print(i)
				break


