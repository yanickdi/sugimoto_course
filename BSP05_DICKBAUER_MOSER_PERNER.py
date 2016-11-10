"""
    BSP 05 - Wuerfelsimulation
    Dickbauer Yanick 1030489, Patrick Moser 1114954, Perner Manuel 0633155
    WS 2016
"""
# INPUT:
MAX_NUMBER_OF_GUESSES = 6

from lib import random_number_from_interval

def main():
    attempt = 0
    right_guesses = 0
    random_die = int(random_number_from_interval(0, 6)+1)
    
    while attempt < 6:
        attempt += 1
        guess = int(input('Rate: '))
        if guess == random_die:
            print('Richtig, du bekommst einen neuen Wuerfel')
            right_guesses += 1
            random_die = int(random_number_from_interval(0, 6)+1)
        else:
            less_or_greater = 'kleiner' if random_die < guess else 'groesser'
            print('Nein, gesuchte Zahl ist {} als {}.'.format(less_or_greater, guess))
    
    # print result
    print('{} mal richtig geraten'.format(right_guesses))
    if right_guesses == 0:
        print('Kein einziges Mal richtig bei {} Versuchen ist halt kein guter Schnitt...'.format(MAX_NUMBER_OF_GUESSES))
    elif right_guesses >= 2:
        print('Super, mindestens zwei mal richtig, gut gemacht!')
        
        
main()