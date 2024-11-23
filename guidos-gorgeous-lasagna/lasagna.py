"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2 
print(EXPECTED_BAKE_TIME)


#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    bake_time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return bake_time_remaining

print(bake_time_remaining(29))
#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider defining a 'PREPARATION_TIME' constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations.

def preparation_time_in_minutes(number_of_layers: int) -> int: 
    """Calculate the prep time in minutes.

    :param number of layers: int - number of layers 
    :return: int - prep time in minutes (in minutes) derived from number of layers.

    Function that takes the actual number of layers of the lasagna and calculates the preparation time
    """
    preparation_time_in_minutes = number_of_layers * PREPARATION_TIME
    return preparation_time_in_minutes

print(preparation_time_in_minutes(3))

#TODO: define the 'elapsed_time_in_minutes()' function below.

def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int: 
    """Calculate the total elapsed time in minutes."""
    elapsed_time_in_minutes = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return elapsed_time_in_minutes

print(elapsed_time_in_minutes(3, 29))



# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)