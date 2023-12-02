str_nums = ['one',
            'two',
            'three',
            'four',
            'five',
            'six',
            'seven',
            'eight',
            'nine']

str_nums_rev = [string[::-1] for string in str_nums]

first_letters = ['otfsen']
last_letters = ['eorxnt']

with open('data.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

total_sum = 0

for string in lines:
    max_index = 0
    first_int = ''
    last_int = ''
    num = ''
    for index, char in enumerate(string):
        curr_index = index
        if char.isnumeric():
            first_int = char
            break
    if first_int:
        for index, char in enumerate(reversed(string)):
            curr_index = index
            if char.isnumeric():
                last_int = char
                break
        curr_num = int(first_int + last_int)
        total_sum += curr_num

print(total_sum)

