from utils import read_input

puzzle = read_input(4)
puzzle_list = []
tmp_list = []
for char in puzzle:
    if char == "\n":
        puzzle_list.append(tmp_list)
        tmp_list = []
        continue
    else:
        tmp_list.append(char)

def traverse_graph(graph):
    res = 0
    ROW = len(graph)
    COL = len(graph[0])

    for row in range(ROW):
        for col in range(COL):
            if check_forklift_access(graph, row, col):
                res += 1
    return res


def check_forklift_access(graph, row, col):
    directions = [(row+1, col), (row-1, col), (row,col+1), (row,col-1)]
    tally = 0
    for direction in directions:
        try:
            if graph[direction[0]][direction[1]] == "@":
                tally += 1
            if tally == 4:
                return False
        except:
            continue
    return True
        


def main():
    # print(traverse_graph(puzzle_list))
    print(len(puzzle))



if __name__ == "__main__":
    main()