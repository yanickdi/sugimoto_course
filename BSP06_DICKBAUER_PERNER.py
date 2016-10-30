"""
    BSP 06 - Manipulierter Wuerfel
    Dickbauer Yanick 1030489, Perner Manuel 0633155
    WS 2016
"""
# INPUT:
RIGGED_DICE_PROBS = (1/10, 1/20, 1/5, 1/10, 1/2, 1/20)
NUMBER_OF_THROWS = 1000

# which number do we want to check
CHECK_DICE = 3
# how often one behind the other
AMOUNT_OF_TANDEMS = 3

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
    count = 0 #result
    subsequent = 0 #how often did we see it at the actual position
    for i in range(NUMBER_OF_THROWS):
        rigged_dice = loaded_random_choice(RIGGED_DICE_PROBS) + 1
        if rigged_dice == CHECK_DICE:
            # we've got one more
            subsequent += 1
            if subsequent >= AMOUNT_OF_TANDEMS:
                count += 1
        else:
            # that's the wrong dice -> set actual amount of subsequents back to zero
            subsequent = 0
            
    print('Anzahl an {} mal hintereinander eine {}: {}'.format(
        AMOUNT_OF_TANDEMS, CHECK_DICE, count))
        
main()