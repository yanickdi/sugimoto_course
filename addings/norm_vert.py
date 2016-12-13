"""
    BSP 15 - ACCEPTANCE-REJECTION METHOD
    Dickbauer Yanick 1030489, Patrick Moser 1114954, Perner Manuel 0633155
    WS 2016
"""

from lib import random_number_from_interval, user_input
from math import pi as pi
from math import exp as exp

DEBUG = True
LIMIT_A = -10
LIMIT_B = 10
M = 0.5

def main():
    number_of_figures = user_input((
        ('Number of figures to be generated', int, 50000), ), DEBUG)[0]
    
    l = []
        
    for i in range(number_of_figures):
        random_figure = rejection_sampling()
        #print(random_figure)
        l.append(random_figure)
    print(sum(l)/len(l))

      
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
    return (1 / (2*pi)**(1/2)) * exp( - (1/2)* x**2)

main()
