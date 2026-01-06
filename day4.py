from utils import read_input

puzzle = read_input(4)
print(puzzle)
puzzle_list = []
tmp_list = []
for char in puzzle:
    if char == "\n":
        puzzle_list.append(tmp_list)
        tmp_list = []
        continue
    else:
        tmp_list.append(char)