# https://github.com/SnoozeySleepy/AdventofCode/blob/main/day1.py
import time

lines = []

with open("part1input.txt", "r") as inputfile:
    for line in inputfile:
        lines.append(int(line.rstrip()))

i = 1

numlarger = 0

t0 = time.time()
while i < len(lines):
    if lines[i] - lines[i - 1] > 0:
        numlarger += 1
    i += 1
t1 = time.time()

print(f"Part 1: {numlarger}, time = {t1 - t0}")

####

i = 0

numlarger = 0

currsum = 0
prevsum = 0

t0 = time.time()
while i < len(lines) - 2:
    currsum = sum(lines[i:i+3])
    if prevsum != 0:
        if currsum > prevsum:
            numlarger += 1
    prevsum = currsum
    i += 1

t1 = time.time()
print(f"Part 2: {numlarger}, time = {t1 - t0}")

