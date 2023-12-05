import re


values = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def part1():
    result = 0
    MATCH = re.compile(r"[a-zA-Z]*(\d).*(\d)[a-zA-Z]*$")
    SHORTMATCH = re.compile(r"[a-zA-Z]*(\d).*$")
    with open("data.txt") as fh_:
        for line in fh_:
            m = MATCH.match(line.strip())
            if m is None:
                n = SHORTMATCH.match(line.strip())
                new = int(n.group(1) * 2)
                result += new
            else:
                new = int(''.join([m.group(1), m.group(2)]))
                result += new
    print(result)


def _get_num(num):
    if num.isdigit():
        return num
    return values[num]


def part2():
    result = 0
    MATCH = re.compile(r"[a-zA-Z]*?(\d|one|two|three|four|five|six|seven|eight|nine).*(\d|one|two|three|four|five|six|seven|eight|nine)[a-zA-Z]*$")
    SHORTMATCH = re.compile(r"[a-zA-Z]*?(\d|one|two|three|four|five|six|seven|eight|nine).*$")
    with open("data.txt") as fh_:
        for line in fh_:
            m = MATCH.match(line.strip())
            if m is None:
                n = SHORTMATCH.match(line.strip())
                new = int(_get_num(n.group(1)) * 2)
                result += new
            else:
                new = int(''.join([_get_num(m.group(1)), _get_num(m.group(2))]))
                result += new
    print(result)

if __name__ == '__main__':
    part1()
    part2()
