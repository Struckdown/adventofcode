f = open("input.txt", "r")
elfHolding = 0
mostElf = 0
for line in f:
    if line == "\n":
        if elfHolding > mostElf:
            mostElf = elfHolding
        elfHolding = 0
        continue
    elfHolding += int(line)

print(mostElf)
