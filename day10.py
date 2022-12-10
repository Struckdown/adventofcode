# Day 10
import queue

signalsToProcess = queue.SimpleQueue()
cycleNumber = 0
delayTillNextInstruction = 0
register = 1
signalStrength = 0

screen = []
for i in range(6):
	row = ["."] * 40
	screen.append(row)

with open('input.txt', 'r') as file:
	for line in file:
		signalsToProcess.put(line)

def processCycle():
	global cycleNumber, delayTillNextInstruction, register, signalStrength, valToAdd
	cycleNumber += 1
	delayTillNextInstruction -= 1

	if (cycleNumber - 20) % 40 == 0:
		print(cycleNumber, register, cycleNumber * register)
		signalStrength += cycleNumber * register

	register += valToAdd
	valToAdd = 0

	if delayTillNextInstruction <= 0:
		if (signalsToProcess.qsize() <= 0):
			return
		line = signalsToProcess.get()
		if "addx" in line:
			data = line.split()
			valToAdd = int(data[1])
			delayTillNextInstruction = 2

	if register >= -1 and register <= 40:
		if abs(cycleNumber%40 - register) <= 1:
			screen[int(cycleNumber/40)][cycleNumber%40] = "#"
	#print(register)

valToAdd = 0
while signalsToProcess.qsize() != 0:
	processCycle()
processCycle()
processCycle()

print(signalStrength)

for row in screen:
	for i in row:
		print(i, end="")
	print()