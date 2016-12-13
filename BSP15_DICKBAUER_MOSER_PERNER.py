"""
    BSP 15 - ACCEPTANCE-REJECTION METHOD
    Dickbauer Yanick 1030489, Patrick Moser 1114954, Perner Manuel 0633155
    WS 2016
"""

from lib import random_number_from_interval, user_input

#INPUT

NUMBER_OF_RANDOM_FIGURES = user_input((
    ('number of figures to be generated', int, 5), ), DEBUG)[0]
LOWER_BOUND = user_input((
    ('Please enter lower bound from 0-3', float, 1), ), DEBUG)[0]
UPPER_BOUND = user_input((
    ('Please enter upper bound from 0-3', float, 3), ), DEBUG)[0]
    
print (NUMBER_OF_RANDOM_FIGURES)
print (LOWER_BOUND)
print (UPPER_BOUND)

#Generate random number X
x = random_number_from_interval(LOWER_BOUND, UPPER_BOUND)

print (x)

#Density Function

def density_function(x):
    x = 0
    if x >= 0:
        return x/4
    elif x >= 1:
        return 1/4
    elif x >= 2:
        return 5/8
    elif x >= 3:
        return 0

# Generate Random Number with Density Function



# Generate Random Uniform Number

