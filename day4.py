# Day 4

# Given two ranges, return if one is a subset of the other
def subset(a, b):
	if (min(a[0], b[0]) == a[0]) and (max(a[-1], b[-1]) == a[-1]):
		return True
	if (min(a[0], b[0]) == b[0]) and (max(a[-1], b[-1]) == b[-1]):
		return True
	return False

# Given two ranges, return if they overlap at all
def overlap(a,b):
	if b[0] in a or b[-1] in a:
		return True
	if a[0] in b or a[-1] in b:
		return True
	return False

count = 0
count2 = 0
with open('input.txt', 'r') as file:
	for line in file:
		elves = line.split(",")
		ranges = elves[0].split("-")
		firstRange = range(int(ranges[0]), int(ranges[1])+1)
		ranges = elves[1].split("-")
		secondRange = range(int(ranges[0]), int(ranges[1])+1)

		# Q1
		count += subset(firstRange, secondRange)

		# Q2
		count2 += overlap(firstRange, secondRange)

print(count)
print(count2)

