import re

def solve():
	f = open("input.txt", "r")
	sum = 0
	regexMapping = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}

	for line in f:
		validNumbersMap = {}
		index = 0

		# Add to the map all digits at their indexes. "jaone2" would add {5: "2"}, saying there is a 2 at index 5
		for char in line:
			if char.isdigit():
				validNumbersMap[index] = char
			index += 1

		# for each mapping, find all occurances and place into the map where the first letter starts using regex
		# eg, if the string is "jaone2", we would place into the map {2: "1"}, meaning at index 2, there is a "1".
		for key in regexMapping:
			regex = re.compile(regexMapping[key])
			iter = regex.finditer(line)
			for match in iter:
				validNumbersMap[match.span()[0]] = key

		# sort values now by index since we filled in the mapping in two different ways
		validNumbersMap = dict(sorted(validNumbersMap.items()))
		
		# convert the mapping into an array so we can access the first and last elements of the array
		arrayForm = []
		for ele in validNumbersMap.values():
			arrayForm.append(ele)
		# and finally sum them
		sum += int(str(arrayForm[0]) + str(arrayForm[-1]))

	# output the answer
	print(sum)

if __name__ == '__main__':
	solve()