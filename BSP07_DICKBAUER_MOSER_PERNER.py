"""
    BSP 07 - Betrunkener
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""
DEBUG = False
POSSIBLE_DIRECTIONS = ( (0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, 1), (1,-1), (-1,-1) )
START_POSITION = (0, 0)

from lib import random_number_from_interval, euclidean_distance, user_input

def main():
    # user input
    (number_of_steps, ) = user_input((
        ('Number of steps', int, 2000), ), DEBUG)
        
    pos = list(START_POSITION)
    for i in range(number_of_steps):
        # get a random direction
        rand_numb = int(random_number_from_interval(0, len(POSSIBLE_DIRECTIONS)))
        direction = POSSIBLE_DIRECTIONS[rand_numb]
        # update current position
        pos[0] += direction[0]
        pos[1] += direction[1]
        
    distance = euclidean_distance(START_POSITION, pos)
    print('Aktueller Punkt ({}, {}) -> {:.2f} EH Entfernung zum Ausgangspunkt.'.format(
        pos[0], pos[1], distance))
    
main()