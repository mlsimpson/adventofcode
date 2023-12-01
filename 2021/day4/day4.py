# Ingest data
# First line is list of numbers drawn :: DONE
# Parse next 5x5 into a grid :: DONE

with open("testinput.txt", "r") as fh:
    # Read first line as list of numbers drawn
    drawn = fh.readline().rstrip().split(",")
    # Read rest of file as the bingo boards
    temp = fh.readlines()

    boardtemp = []

    # Remove "\n"
    # Convert string of nums to list of ints
    for line in temp:
        line = line.rstrip()
        line = [int(i) for i in line.split()]
        # Remove empty
        if line:
            boardtemp.append(line)

    # Remove blank entries
    # boardtemp = [i for i in boardtemp if i]

# Put 5 lines into a new 'board' structure
# Repeat until all lines are in board structures

boards = []

boards = [boardtemp[i:i+5] for i in range(0, len(boardtemp), 5)]

# for i in range(0, len(boardtemp), 5): boards.append(boardtemp[i:i+5])

# def makeboard(rows, startindex):
#     i = 0
#
#     board = []
#
#     while i < 5:
#         board.append(rows[startindex + i])
#         i += 1
#
#     return board
#
# def makeboards(rows):
#     index = 0
#
#     while index < len(rows):
#         boards.append(makeboard(rows, index))
#         index += 5
#
#     return boards
#
# boards = makeboards(boardtemp)

print(boards)

# For each number called:
# - Check boards for number
# - Replace number on grids with an "X"
# - Check each board for win condition
#    - win condition is row or column. diagonals don't count
#
# On winning board, add all unmarked numbers, then multiply that by last
# number called


