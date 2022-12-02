def solve():
    f = open("input.txt", "r")
    elfHolding = 0
    allElves = []
    for line in f:
        if line == "\n":
            allElves.append(elfHolding)
            elfHolding = 0
            continue
        elfHolding += int(line)

    allElves.sort()
    print(allElves)
    print(sum(allElves[-3:]))

if __name__ == '__main__':
    solve()