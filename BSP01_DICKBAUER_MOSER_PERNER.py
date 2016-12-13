"""
    BSP 01 - Integrierte Zufallszahlen
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""
DEBUG = False


from lib import random_number_from_interval, user_input

def main():
    # get user input:
    number_of_random_values, interval_from, interval_to = user_input((
            ('Number of random values', int, 10),
            ('Interval from', float, 2.0),
            ('Interval to',   float, 4.0)), use_defaults=DEBUG)
    
    # for every i in {0..random_number_from_interval-1}:
    for i in range(number_of_random_values):
        # generate a new random val between interval_from and interval to
        value = random_number_from_interval(interval_from, interval_to)
        print('{:.2f}'.format(value))

        
main()
