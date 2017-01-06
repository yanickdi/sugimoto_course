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

class Product:
    def __init__(self, type, processing_time):
        self.type = type
        self.processing_time = processing_time
        self.remaining_time = processing_time

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
    """Generates a product and returns a Product"""
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
    product_in_machine = None
    nr_eliminated = 0
    nr_finished_products = 0
    for t in range( int(SIM_STEPS_PER_HOUR * 8) ): #8h
        # the queue part:
        if time_until_next_product == 0:
            # create a new product, append to queue and wait for the next one
            product = generate_product()
            if len(queue) + 1 > MAX_QUEUE_LENGTH:
                # eliminate!
                nr_eliminated += 1
            else:
                queue.append(product)
            time_until_next_product = generate_time_until_next_product()
        else:
            time_until_next_product -= 1
            
        #the production part: we can serve only one product at once
        if product_in_machine == None and len(queue) > 0:
            # take the first out of the queue and start to process it
            product_in_machine = queue.pop(0)
        else:
            # there is a product in the queue, reduce its processing time
            product_in_machine.remaining_time -= 1
            # is the product now finished?
            if product_in_machine.remaining_time == 0:
                # remove product and take the next product out of the queue
                product_in_machine = None
                nr_finished_products += 1
                if len(queue) > 0: product_in_machine = queue.pop(0)
                
    print('Finished products: ', nr_finished_products)
    print('Eliminated products: ', nr_eliminated)
main()











