import sys

sys.path.insert(0, '.')

from src.utils.tools import read_input


def process_main_data(day_number, part, test):

    data_input_lst = read_input(day_number, part_=part, test=test, sep="\n")
    data_prepared = [list(game_) for game_ in data_input_lst]

    return data_prepared


def extract_numbers(data, start_digit, end_digit):
    result = []
    current_number = []

    for digit in data:
        if digit.isdigit():
            current_number.append(digit)
        elif current_number and current_number[0] == start_digit and current_number[-1] == end_digit:
            result.append(int(''.join(current_number)))
            current_number = []
        else:
            current_number = []

    return result


def get_full_digit(data_, new_row, new_col):

    final_digit = data_[new_row][new_col]

    # go left
    if new_col != 0:
        for col_left in reversed(range(new_col)):
            if data_[new_row][col_left].isdigit():
                final_digit = data_[new_row][col_left] + final_digit
            else:
                break

    # go right
    if len(data_[0]) - new_col != 0:
        for col_right in range(new_col+1, len(data_[0])):
            if data_[new_row][col_right].isdigit():
                final_digit = final_digit + data_[new_row][col_right]
            else:
                break

    return int(final_digit)


def are_adjacent_digits(data_, row_, col_):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    # Iterate through each direction
    digits_result = []
    for dr, dc in directions:
        new_row, new_col = row_ + dr, col_ + dc

        # Check if the new position is within the matrix bounds
        if 0 <= new_row < len(data_) and 0 <= new_col < len(data_[0]):
            # Check if the adjacent element is a digit
            if data_[new_row][new_col].isdigit():
                result_ = get_full_digit(data_, new_row, new_col)
                digits_result.append(result_)
    return list(set(digits_result))


def challenge_day_3_part_1(data_):

    final_list_score = []
    for row_ in range(0, len(data_)):
        for col_ in range(0, len(data_[0])):
            if not data_[row_][col_].isdigit() and data_[row_][col_] != ".":
                result_ = are_adjacent_digits(data_, row_, col_)
                final_list_score += result_

    final_score = sum(final_list_score)

    return final_score


def run_tests():
    print(f"\nRunning Tests:")
    assert challenge_day_3_part_1(process_main_data(3, 1, test=True)) == 4361
    #assert challenge_day_2_part_2(process_main_data(2, 1, test=True)) == 2286
    print("ALL GOOD")


def run_solution():
    print(f"\nRunning Solutions: \n------------------")
    answer1 = challenge_day_3_part_1(process_main_data(3, 1, test=False))
    print(f"Answer part1: {answer1}")
    #answer2 = challenge_day_2_part_2(process_main_data(2, 1, test=False))
    #print(f"Answer part2: {answer2}")

if __name__ == "__main__":
    run_tests()
    run_solution()
