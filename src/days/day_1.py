import sys

sys.path.insert(0, '.')

from src.utils.tools import read_input


def process_main_data(day_number, part, test):

    data_input_lst = read_input(day_number, part_=part, test=test, sep="\n")

    return data_input_lst


def challenge_day_1_part_1(data_input_lst):

    final_result = 0
    for text_ in data_input_lst:

        lst_digit = [char_ for char_ in text_ if char_.isdigit()]
        final_digit = int(lst_digit[0]+lst_digit[-1])

        final_result += final_digit

    return final_result


    words = ''.join([char if char.isalpha() else ' ' for char in "4nineeightseven2"]).split()
    digits = ''.join([char if char.isdigit() else '' for char in "4nineeightseven2"])



def run_tests():
    print(f"\nRunning Tests:")
    assert challenge_day_1_part_1(process_main_data(1, 1, test=True)) == 142
    assert challenge_day_1_part_1(process_main_data(1, 2, test=True)) == 281
    print("ALL GOOD")


def run_solution():
    print(f"\nRunning Solutions: \n------------------")
    answer1 = challenge_day_1_part_1(process_main_data(1, 1, test=False))
    print(f"Answer part1: {answer1}")

if __name__ == "__main__":
    run_tests()
    run_solution()