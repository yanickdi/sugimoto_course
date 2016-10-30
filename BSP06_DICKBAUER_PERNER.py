"""
    BSP 06 - Manipulierter Wuerfel
    Dickbauer Yanick 1030489, Perner Manuel 0633155
    WS 2016
"""
# INPUT:
RIGGED_DICE_PROBS = (1/10, 1/20, 1/5, 1/10, 1/2, 1/20)

#from lib import random_number_from_interval
import random

def loaded_random_choice(probability_list):
    """This stochastic function takes a list as input and returns a random index corresponding to the list.
    The randomness of the index is loaded: the probality of choosing an index is exactly the corresponding
    probability given at this index position of the input lix.
    e.g.: [0.2, 0.8] --> the return value of `0` is 20% likely, the return value of `1` is 80% likely
    note that the sum of all values in the `probability_list` has to be 1
    """
    n = len(probability_list)
    random_number = random.random()
    cum_p = 0
    for i in range(n):
        cum_p += probability_list[i]
        if cum_p > random_number:
            return i
    return None
    

def main():
    rigged_dice = loaded_random_choice(RIGGED_DICE_PROBS) + 1
    print(rigged_dice)
        
main()