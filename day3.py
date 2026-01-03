from utils import read_input

puzzle = read_input(3)
bank_list = []
start_idx = 0

for idx, num in enumerate(puzzle):
    if num == "\n":
        bank_list.append(puzzle[start_idx:idx]) if start_idx == 0 else bank_list.append(puzzle[start_idx+1:idx])
        start_idx = idx

def calculate_joltage(bank):
    check_set = set()
    max_joltage = 0
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            joltage = int(bank[i] + bank[j])
            if joltage > max_joltage:
                max_joltage = joltage
    return max_joltage


def main():
    total_output_joltage = 0
    for bank in bank_list:
        total_output_joltage += calculate_joltage(bank)
    print(total_output_joltage)


if __name__ == "__main__":
    main()
    