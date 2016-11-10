"""
    BSP 01 - Integrierte Zufallszahlen
    Dickbauer Yanick 1030489, Patrick Moser 1114954, Perner Manuel 0633155
    WS 2016
"""
# INPUT:
NUMBER_OF_RANDOM_VALUES = 10
INTERVAL = [2, 4]


from lib import random_number_from_interval

def main():
    for i in range(NUMBER_OF_RANDOM_VALUES):
        value = random_number_from_interval(INTERVAL[0], INTERVAL[1])
        print('{:.2f}'.format(value))

        
main()
"test"