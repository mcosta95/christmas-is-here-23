import sys

sys.path.insert(0, '.')

from src.utils.tools import read_input


day_number = 1

data_input_lst = read_input(day_number, test=True, sep="\n")


if __name__ == "__main__":
    run_tests()
    run_solution()