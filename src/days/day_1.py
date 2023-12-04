"""--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine -> 29
eightwothree -> 83
abcone2threexyz -> 13
xtwone3four -> 24
4nineeightseven2 -> 42
zoneight234 -> 14
7pqrstsixteen -> 76
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?"""

import sys
from word2number import w2n
import re
import nltk

sys.path.insert(0, '.')

from src.utils.tools import read_input

def process_main_data(day_number, part, test):

    data_input_lst = read_input(day_number, part_=part, test=test, sep="\n")

    return data_input_lst

data = process_main_data(1, 2, test=True)

words_numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


str_ = data[1]

#for i in str_:
#output_lst = [words_numbers[value] for value in words_numbers.keys() if value in str_]

[words_numbers[value] for value in sorted(words_numbers, key=str_.index)]


output_lst = [value for key_, value  in words_numbers.items() if str(value) in str_ or key_ in str_]

output_lst.sort(key=lambda x: str_.index(next(key for key, value in words_numbers.items() if value == x)))

for nr_letter, number_ in words_numbers.items():
    if str(nr_letter) in str_:



    str_ = str_.replace(nr_letter, str(number_))




data = 1

#w2n.word_to_num(word) for word in s.split()

# Separate words and digits


# Convert words to numbers
# numeric_value = sum(w2n.word_to_num(word) for word in words)

# Combine numeric value with digits
# result = str(numeric_value) + digits

def challenge_day_1_part_1(data_input_lst):

    final_result = 0
    for text_ in data_input_lst:

        lst_digit = [char_ for char_ in text_ if char_.isdigit()]
        final_digit = int(lst_digit[0]+lst_digit[-1])

        final_result += final_digit

    return final_result


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