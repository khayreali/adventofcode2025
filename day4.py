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

res = 0

def traverse_graph(graph):
    ROW = len(graph)
    COL = len(graph[0])

    # for row in range(ROW):
    #     for col in range(COL):
    #         # if check_forklift_access(row, col):
    #         #     res += 1
    return res


# def check_forklift_access(row, col)
#     directions = [row-1, row+1, col-1, col+1]
#     for direction in directions:
        


def main():
    return traverse_graph(puzzle_list)



if __name__ == "__main__":
    main()