"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time



def preparation_time_in_minutes(number_of_layers):
    """Calculate the amount of preparation time based on layers

    :param number_of_layers int - the number of lasagna layers to prep
    :return int - minutes of required preparation

    Function that takes the number of desired layers as an argument 
    and returns the amount of minutes needed to prep that many layers
    based on the PREPARATION_TIME
    """

    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time

    :param number_of_layers: int - the amount of layers for the lasagna
    :param elapsed_bake_time: int - amount of minutes the lasagna has already baked
    :return: int - total time spent preparing and baking

    Function that takes in two parameters: number_of_layers and elapsed_bake_time, and
    give the total elapsed time spent making the lasagna so far
    """


    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time