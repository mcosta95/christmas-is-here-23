import sys

sys.path.insert(0, '.')

from src.utils.tools import read_input

def process_main_data(day_number, part, test):

    data_input_lst = read_input(day_number, part_=part, test=test, sep="\n")
    data_prepared = [game_.split(":")[1].split(";") for game_ in data_input_lst]

    return data_prepared


def challenge_day_2_part_1(data_input_lst):

    rule_ = {"red": 12, "green": 13, "blue": 14}

    final_score = 0
    for game_idx in range(0, len(data_input_lst)):

      game_part = [str_.strip().split(", ") for str_ in data_input_lst[game_idx]]

      round_score = []
      for round_ in game_part:
        if sum([int(instance_.split(" ")[0]) > rule_[instance_.split(" ")[1]] for instance_ in round_]):
            round_score.append(True)
        else:
            round_score.append(False)

      if sum(round_score) == 0:
          final_score += game_idx + 1

    return final_score


def challenge_day_2_part_2(data_input_lst):

    final_score = 0
    for game_idx in range(0, len(data_input_lst)):

        game_part = [str_.strip().split(", ") for str_ in data_input_lst[game_idx]]
        max_values = {'blue': 0, 'red': 0, 'green': 0}

        for inner_list in game_part:
            for item in inner_list:
                value_str, color = item.split(" ")
                value = int(value_str)
                max_values[color] = max(max_values[color], value)

        
        result = 1
        for value in max_values.values(): 
            result *= value

        final_score += result

    return final_score



def run_tests():
    print(f"\nRunning Tests:")
    assert challenge_day_2_part_1(process_main_data(2, 1, test=True)) == 8
    assert challenge_day_2_part_2(process_main_data(2, 1, test=True)) == 2286
    print("ALL GOOD")


def run_solution():
    print(f"\nRunning Solutions: \n------------------")
    answer1 = challenge_day_2_part_1(process_main_data(2, 1, test=False))
    print(f"Answer part1: {answer1}")
    answer2 = challenge_day_2_part_2(process_main_data(2, 1, test=False))
    print(f"Answer part2: {answer2}")

if __name__ == "__main__":
    run_tests()
    run_solution()
