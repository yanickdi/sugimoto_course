"""
    BSP 15 - Inversionsmethode
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""

from lib import random_number_from_interval, user_input
DEBUG = False

def main():
    
    amount_of_random_numbers = user_input([['Please enter the desired amount of random numbers', int, 10]], DEBUG)[0]
    
    for i in range(amount_of_random_numbers):
        rand = random_number_from_interval(0,1)
        random_number = (1/(1-rand)-1)**(1/2)
        print(random_number)

main()