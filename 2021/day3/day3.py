lines = []

with open("input.txt", "r") as fh:
    for line in fh:
        lines.append(list(map(int, list(line.rstrip()))))

def bintodec(number):
    return int(''.join(str(i) for i in number), 2)

gamma = []
epsilon = []
i = 0

while i < len(lines[0]):
    ones = 0
    zeroes = 0
    for line in lines:
        if line[i] == 1:
            ones += 1
        else:
            zeroes += 1

    if ones > zeroes:
        gamma.append(1)
        epsilon.append(0)
    else:
        gamma.append(0)
        epsilon.append(1)

    i += 1

gamma = bintodec(gamma)
epsilon = bintodec(epsilon)

print(gamma * epsilon)

####

def countbits(numbers, index):
    ones = 0
    zeroes = 0

    for num in numbers:
        if num[index] == 0:
            zeroes += 1
        else:
            ones += 1

    return zeroes, ones

def filternums(numbers, bitvalue, index):
    new_numbers = []

    for num in numbers:
        if num[index] == bitvalue:
            new_numbers.append(num)

    return new_numbers

def rating(numbers, index, mode):
    if len(numbers) == 1:
        return numbers[0]

    zeroes, ones = countbits(numbers, index)

    if ones > zeroes or ones == zeroes:
        if mode == "oxygen":
            numbers = filternums(numbers, 1, index)
        else:
            numbers = filternums(numbers, 0, index)
    else:
        if mode == "oxygen":
            numbers = filternums(numbers, 0, index)
        else:
            numbers = filternums(numbers, 1, index)

    return rating(numbers, index + 1, mode)

# def oxygen(numbers, index):
#     if len(numbers) == 1:
#         return numbers[0]
#
#     zeroes, ones = countbits(numbers, index)
#
#     if ones > zeroes or ones == zeroes:
#         # filter on 1 in index
#         numbers = filternums(numbers, 1, index)
#     else:
#         # filter on 0 in index
#         numbers = filternums(numbers, 0, index)
#
#     return oxygen(numbers, index + 1)
#
# def co2(numbers, index):
#     if len(numbers) == 1:
#         return numbers[0]
#
#     zeroes, ones = countbits(numbers, index)
#
#     if ones > zeroes or ones == zeroes:
#         # filter on 0 in index
#         numbers = filternums(numbers, 0, index)
#     else:
#         # filter on 1 in index
#         numbers = filternums(numbers, 1, index)
#
#     return co2(numbers, index + 1)

oxygennum = rating(lines, 0, "oxygen")
oxygennum = bintodec(oxygennum)

co2num = rating(lines, 0, "co2")
co2num = bintodec(co2num)

print(oxygennum * co2num)

