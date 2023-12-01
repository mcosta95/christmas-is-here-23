import os

def read_input(day_number, part_, test=True, sep="\n"):
    """
    Read input data from a file for a given day.

    Parameters:
        day_number (int): The day number for which to read the input data.
        part_ (int): The part of the challenge.
        test (bool, optional): Whether to read test data (default is True).
        sep (str, optional): The separator to split the input data (default is "\n").

    Returns:
        list: A list containing lines of input data.
    """
    current_directory = os.getcwd()
    file_name = f"day_{day_number}_part_{part_}.txt"

    folder_name = "data_test" if test else "main_data"

    path_to_file = os.path.join(current_directory, "data", folder_name, file_name)
    
    with open(path_to_file, "r") as file:
        data_input = file.read().split(sep)

    return data_input