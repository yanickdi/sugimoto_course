"""
    BSP 15 - Verwerfungsmethode
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""

from lib import random_number_from_interval, user_input
DEBUG = False
OPTION = True

LIMIT_A = 0
LIMIT_B = 3
M = 5/8 + 0.001

def main():
    number_of_figures = user_input((
        ('Number of figures to be generated', int, 10), ), DEBUG)[0]
    
    accepted_figures = []
        
    for i in range(number_of_figures):
        random_figure = rejection_sampling()
        print(random_figure)
        accepted_figures.append(random_figure)
        
    if OPTION:
        print('\nAverage of all random figures:', sum(accepted_figures)/number_of_figures)

      
def rejection_sampling():
    while True:
        #Generate random number X
        zz1 = random_number_from_interval(LIMIT_A, LIMIT_B)
        zz2 = random_number_from_interval(0, M)
        if zz2 > density_function(zz1):
            # reject
            pass
        else:
            return zz1

def density_function(x):
    if x >= 3:
        return 0
    elif x >= 2:
        return 5/8
    elif x >= 1:
        return 1/4
    else:
        return x/4

main()
