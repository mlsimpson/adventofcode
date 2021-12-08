lines = []

with open("input.txt", "r") as fh:
    for line in fh:
        lines.append(line.rstrip())

horizpos = 0
vertpos = 0

for instruction in lines:
    tmp = instruction.split()
    direction = tmp[0]
    units = int(tmp[1])

    if direction == "forward":
        horizpos += units
    elif direction == "down":
        vertpos += units
    else:
        vertpos -= units

print(f"Part 1: {horizpos * vertpos}")

####

horizpos = 0
vertpos = 0
aim = 0

for instruction in lines:
    tmp = instruction.split()
    direction = tmp[0]
    units = int(tmp[1])

    if direction == "forward":
        horizpos += units
        vertpos += (aim * units)
    elif direction == "down":
        aim += units
    else:
        aim -= units

print(f"Part 2: {horizpos * vertpos}")

