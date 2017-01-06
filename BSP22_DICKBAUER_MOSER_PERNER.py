"""
    BSP 22 - Fertigungssystem
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""
from collections import namedtuple
from lib import random_exp, random_number_from_interval, loaded_random_choice

SIM_FREQUENCY = 1 # or simulation intervals per second
SIM_STEPS_PER_HOUR = SIM_FREQUENCY * 60 * 60

PROD_TYPE_1 = 0
PROD_TYPE_2 = 1

MAX_QUEUE_LENGTH = 5

Product = namedtuple('Product', ['type', 'processing_time'])

def generate_processing_time(product_type):
    """Returns a simulated processing time in simulation intervals for a product of type `product_type`"""
    # processing_time is equally distributed between a lb/ub:
    if product_type == PROD_TYPE_1:
        minutes = random_number_from_interval(2, 6)
    elif product_type == PROD_TYPE_2:
        minutes = random_number_from_interval(1.5, 4.5)
    else:
        raise ValueError()
    return int(minutes * 60 * SIM_FREQUENCY)
        
def generate_product():
    """Generates a product and returns a `Product` tuple (defined at the top of
    this file - like a struct in C ;-) )"""
    # type is rigged - 0.4 probabilty for type 1, 0.6 type 2
    choice_index = loaded_random_choice([0.4, 0.6])
    type = [PROD_TYPE_1, PROD_TYPE_2][choice_index]
    # its related processing time:
    processing_time = generate_processing_time(type)
    # create a namedtuple and return the sh**
    return Product(type, processing_time)
    
def generate_time_until_next_product():
    # the amount of products is exponential distributed having an expected value of 4 minutes
    return int(random_exp(4) * 60 * SIM_FREQUENCY)
    

def main():
    # simulate 8h in intervals of seconds:
    queue = []
    time_until_next_product = 0
    for t in range(SIM_STEPS_PER_HOUR * 8): #8h
        if time_until_next_product == 0:
            # create a new product, append to queue and wait for the next one
            product = generate_product()
            queue.append(product)
            time_until_next_product = generate_time_until_next_product()
        else:
            time_until_next_product -= 1
    print(len(queue))
main()











