import random

def random_number_from_interval(lower, upper):
    """Returns a random number out of the interval [lower, upper]"""
    val = random.random()
    return lower + (upper -lower) * val