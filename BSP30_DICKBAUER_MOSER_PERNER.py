"""
    BSP 30 - Supermarkt
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""
from lib import random_exp

FREQUENCY = 1 # simulations per minute
SIM_DURATION = 100
NR_SIM_STEPS = int(FREQUENCY * SIM_DURATION)

CUST_TYPE_NORMAL = 0
CUST_TYPE_EXPRESS = 1

def generate_next_customer_time(cust_type):
    if cust_type == CUST_TYPE_NORMAL:
        rand = random_exp(3)
    elif cust_type == CUST_TYPE_EXPRESS:
        rand = random_exp(5)
    time = int(rand * FREQUENCY)
    if time == 0:
        print('warning, increase simulation frequency')
        time = 1
    return time
    
def generate_service_time(cust_type):
    if cust_type == CUST_TYPE_NORMAL:
        rand = random_exp(5)
    elif cust_type == CUST_TYPE_EXPRESS:
        rand = random_exp(3)
    time = int(rand * FREQUENCY)
    if time == 0:
        print('warning, increase simulation frequency')
        time = 1
    return time

def check_cash_desk(queues, rem_service_times):
    for desk_type in rem_service_times:
        for desk_nr, rem_service_time in enumerate(rem_service_times[desk_type]):
            # is this desk idle just finished a customer?
            queue_before_desk = queues[desk_type][desk_nr]
            if rem_service_time == None or rem_service_time == 0:
                if rem_service_time == 0:
                    # this customer is done
                    rem_service_times[desk_type][desk_nr] = None
                    print('just finished a customer')
                
                # we can serve the next customer
                if len(queue_before_desk) > 0:
                    next_customer_type = queue_before_desk.pop(0)
                    next_service_time = generate_service_time(next_customer_type)
                    rem_service_times[desk_type][desk_nr] = next_service_time
    
def simulate_cash_desks(nr_normal_desk, nr_expess_desk):
    # initialize empty queues for each desk
    types = [('normal', nr_normal_desk), ('express', nr_expess_desk)]
    queues  = {key: [[] for i in range(nr)] for key, nr in types}
    rem_service_times = {key: [None for i in range(nr)] for key, nr in types}
    
    for t in range(NR_SIM_STEPS):
        # check desks if one is idle or just finished a customer
        check_cash_desk(queues, rem_service_times)
        
        # finished iteration, decrease all times:
        for rem_time_list in rem_service_times.values():
            for i, time in enumerate(rem_time_list):
                rem_time_list[i] = time - 1 if time is not None else None

def main():
    simulate_cash_desks(1, 2)
    
main()