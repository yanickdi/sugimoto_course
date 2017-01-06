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
    """This class is only a wrapper for some data in it - like a struct in c/c++"""
    def __init__(self, type, processing_time):
        self.type = type
        self.processing_time = processing_time
        self.inspection_time = None # will be set maybe later

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
    
def generate_inspection_time(product_type):
    """Returns a simulated inspection time in simulation intervals for a product of type `product_type`"""
    # inspection_time is equally distributed between a lb/ub
    if product_type == PROD_TYPE_1:
        minutes = random_number_from_interval(3, 5)
    elif product_type == PROD_TYPE_2:
        minutes = random_number_from_interval(1, 3)
    else:
        raise ValueError()
    return int(minutes * 60 * SIM_FREQUENCY)
    
def is_product_defect(product):
    """Returns True or False """
    # probabilty to be defect is 0.1 - we use our loaded_random_choice function
    return [True, False][loaded_random_choice([0.1, 0.9])]
        
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
    

def simulate_system(hours):
    queue = []
    inspection_queue = []
    time_until_next_product = 0
    product_in_machine = None
    remaining_processing_time = None
    product_in_inspection = None
    remaining_inspection_time = None
    
    nr_eliminated = 0
    nr_finished_products = 0
    nr_finished_system = 0
    nr_defect_products = 0
    
    for t in range( int(SIM_STEPS_PER_HOUR * hours) ):
        # THE QUEUE PART:
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
        
        #THE PRODUCTION PART: we can serve only one product at once
        if product_in_machine == None and len(queue) > 0:
            # take the first out of the queue and start to process it
            product_in_machine = queue.pop(0)
            remaining_processing_time = product_in_machine.processing_time
        else:
            # there is a product in the queue, reduce its processing time
            remaining_processing_time -= 1
            # is the product now finished?
            if remaining_processing_time == 0:
                # remove product out of the machine, push it to the inspection_queue
                # and take the next product out of the processing queue:
                product_in_machine.inspection_time = generate_inspection_time(product_in_machine.type)
                inspection_queue.append(product_in_machine)
                product_in_machine = None
                nr_finished_products += 1
        
        #THE INSPECTION PART: we can only inspect one product at once but its queue is not limited:
        if product_in_inspection == None and len(inspection_queue) > 0:
            # take the first out of the inspection queue and start to inspect it
            product_in_inspection = inspection_queue.pop(0)
            remaining_inspection_time = product_in_inspection.inspection_time
        elif product_in_inspection != None:
            remaining_inspection_time -= 1
            if remaining_inspection_time == 0:
                # remove product out of the inspection
                nr_finished_system += 1
                nr_defect_products += 1 if is_product_defect(product_in_inspection) else 0
                product_in_inspection = None
        else:
            # nothing to do on the inspection machine
            pass
            
        
    print('Finished products: ', nr_finished_products)
    print('Eliminated products: ', nr_eliminated)
    print('Products that finished the system:', nr_finished_system)
    print('Inspection queue length: ', len(inspection_queue))
    if remaining_inspection_time is not None and remaining_inspection_time > 0:
        print('One product is still in inspection')
    
def main():
    print('Starting the warming phase (8 hours):')
    simulate_system(8) #warming phase (not sure why we do this since we delete all variables after it..)
    return
    for i in range(5): print()
    print('Starting the real simulation (800h):')
    simulate_system(800)
main()











