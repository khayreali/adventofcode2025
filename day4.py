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
    if graph[row][col] != "@":
        return False
    
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    tally = 0
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(graph) and 0 <= new_col < len(graph[0]):
            if graph[new_row][new_col] == "@":
                tally += 1
    return tally < 4
        


def main():
    print(traverse_graph(puzzle_list))



if __name__ == "__main__":
    main()