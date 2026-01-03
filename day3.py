from utils import read_input

puzzle = read_input(3)
bank_list = puzzle.split("\n")


def calculate_joltage(bank, num_digits=12):
    n = len(bank)
    result = []
    start = 0
    
    for i in range(num_digits):
        digits_remaining_to_pick = num_digits - i
        end = n - digits_remaining_to_pick
        
        max_digit = '0'
        max_pos = start
        for pos in range(start, end + 1):
            if bank[pos] > max_digit:
                max_digit = bank[pos]
                max_pos = pos
        
        result.append(max_digit)
        start = max_pos + 1
    
    return int(''.join(result))


def main():
    total_output_joltage = 0
    for bank in bank_list:
        total_output_joltage += calculate_joltage(bank)
    print(total_output_joltage)


if __name__ == "__main__":
    main()
    