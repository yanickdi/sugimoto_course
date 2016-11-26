"""
    BSP13 - Simulation von PI
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
    
    Comment: see Monte-Carlo-Simulation Wikipedia
"""

from lib import random_number_from_interval, euclidean_distance


# INPUT:
SIMULATIONS = 100000
REFERENCE_PI = 3.14159265

def main():
    count = 0 # how often did we shoot in the unit circle
    
    for i in range(SIMULATIONS):
        # create two randoms representing cords in a [1,1] rectangle
        x = random_number_from_interval(0,1)
        y = random_number_from_interval(0,1)
        # check wheter these cords are lying within or beyond the unit circle
        if euclidean_distance((0, 0), (x, y)) <= 1:
            count += 1
        
    # avg_occurrences p should be pi/4 / 1 --> 4 * avg = pi
    avg_occurrences = count/SIMULATIONS
    pi = avg_occurrences * 4
    print('Pi is simulated:', pi)
    print('Difference:     {:+.5f} %'.format((pi/REFERENCE_PI - 1) * 100))
   
main()