"""
    BSP 30 - Supermarkt
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""
from itertools import chain # this import from python's stdlibrary
                            # makes our simulation a little bit faster, i hope its ok
from lib import random_exp, _dbg

DEBUG = False
PRINT_EVERY_STEP = False
PLOT = False

FREQUENCY = 1 # simulations per minute
SIM_DURATION = 100
NR_SIM_STEPS = int(FREQUENCY * SIM_DURATION)

NORMAL = 'normal'
EXPRESS = 'express'

def save_it_data(it_data, queues, rem_service_times):
    """ saves all relevant data of the actual iteration to the it_data list """
    t = len(it_data)
    normal_queue_lengths = [len(q) for q in queues[NORMAL]]
    express_queue_lengths = [len(q) for q in queues[EXPRESS]]
    all_queue_lengths = normal_queue_lengths + express_queue_lengths
    normal_utilizations = [0 if s is None else 1 for s in rem_service_times[NORMAL]]
    express_utilizations = [0 if s is None else 1 for s in rem_service_times[EXPRESS]]
    all_utilizations = normal_utilizations + express_utilizations
    if t == 0:
        cum_queue_length_normal = sum(normal_queue_lengths)
        cum_queue_length_express = sum(express_queue_lengths)
    else:
        cum_queue_length_normal = it_data[t-1]['cum_queue_length_normal'] + sum(normal_queue_lengths)
        cum_queue_length_express = it_data[t-1]['cum_queue_length_express'] + sum(express_queue_lengths)
    it_data.append({
        'normal_queue_lengths' : normal_queue_lengths,
        'express_queue_lengths' : express_queue_lengths,
        'all_queue_lengths' : all_queue_lengths,
        'normal_utilizations' : normal_utilizations,
        'express_utilizations' : express_utilizations,
        'all_utilizations' : all_queue_lengths,
        'cum_queue_length_normal' : cum_queue_length_normal,
        'cum_queue_length_express' : cum_queue_length_express
        })

def generate_next_customer_arrival(cust_type):
    if cust_type == NORMAL:
        rand = random_exp(3)
    elif cust_type == EXPRESS:
        rand = random_exp(5)
    time = int(rand * FREQUENCY)
    if time == 0:
        _dbg('warning, increase simulation frequency', DEBUG)
        time = 1
    return time
    
def generate_service_time(cust_type):
    if cust_type == NORMAL:
        rand = random_exp(5)
    elif cust_type == EXPRESS:
        rand = random_exp(3)
    time = int(rand * FREQUENCY)
    if time == 0:
        _dbg('warning, increase simulation frequency', DEBUG)
        time = 1
    return time

def check_cash_desk(queues, rem_service_times):
    """ Checks each cash desk - if one is free, it will serve the next of its queue """
    for desk_type in rem_service_times:
        for desk_nr, rem_service_time in enumerate(rem_service_times[desk_type]):
            # is this desk idle just finished a customer?
            queue_before_desk = queues[desk_type][desk_nr]
            if rem_service_time == None or rem_service_time == 0:
                if rem_service_time == 0:
                    # this customer is done
                    rem_service_times[desk_type][desk_nr] = None
                    _dbg('just finished a customer', DEBUG)
                
                # we can serve the next customer
                if len(queue_before_desk) > 0:
                    next_customer_type = queue_before_desk.pop(0)
                    next_service_time = generate_service_time(next_customer_type)
                    rem_service_times[desk_type][desk_nr] = next_service_time

def check_new_arrivals(next_arrivals, queues):
    """
        Checks if there is a new customer arriving - if yes - attach her to
        the shortest (allowed) queue
    """
    def _best_queue(type, queue):
        if type == NORMAL:
            # this customer can only choose between normal queues
            possible_queues = queues[NORMAL]
        elif type == EXPRESS:
            # this customer can choose between normal queues and of course - express queues
            possible_queues = chain(queues[EXPRESS], queues[NORMAL])
        # now lookup the shortest queue
        return min(possible_queues, key=lambda q: len(q))
    
    for type, arrival in next_arrivals.items():
        if arrival == 0:
            _dbg('customer of type {} arrived'.format(type), DEBUG)
            # a new customer of type `type` arrived - add her to best queue
            shortest_queue = _best_queue(type, queues)
            shortest_queue.append(type)
            # create a new arrival:
            next_arrivals[type] = generate_next_customer_arrival(type)
    
def print_status(t, queues, rem_service_times):
    print('Iteration :{}'.format(t))
    for type in (NORMAL, EXPRESS):
        for desk_nr in range(len(queues[type])):
            queue = queues[type][desk_nr]
            rem_time = rem_service_times[type][desk_nr]
            rem_time_str = 'no customer' if rem_time is None else str(rem_time)
            print('  {} desk #{}'.format(type, desk_nr+1))
            print('     queue length: {}'.format(len(queue)))
            print('     rem_service_time of actual customer: {}'.format(rem_time_str))
    print()

def plot_simulation(it_data):
    import matplotlib.pyplot as plt
    try: import seaborn as sns
    except: pass
    nr_normal_desk = len(it_data[0]['normal_queue_lengths'])
    nr_express_desk = len(it_data[0]['express_queue_lengths'])
    
    plt.title('Amount of normal desks: {}, express desks: {}'.format(nr_normal_desk, nr_express_desk))
    
    avg_queue_normal = [it['cum_queue_length_normal'] / (nr_normal_desk * t+1)
                            for t, it in enumerate(it_data)]
    plt.plot(avg_queue_normal, label='Avg. Queue Length Normal Desks')
    
    if nr_express_desk > 0:
        avg_queue_express = [it['cum_queue_length_express'] / (nr_normal_desk * t+1)
                                for t, it in enumerate(it_data)]
        plt.plot(avg_queue_express, label='Avg. Queue Length Express Desks')
        
    plt.legend()
    plt.show()
    
def simulate_cash_desks(nr_normal_desk, nr_expess_desk):
    # initialize empty queues for each desk
    types = [(NORMAL, nr_normal_desk), (EXPRESS, nr_expess_desk)]
    queues  = {key: [[] for i in range(nr)] for key, nr in types}
    rem_service_times = {key: [None for i in range(nr)] for key, nr in types}
    next_arrivals = {key: 0 for key, nr in types} # at the beginning of sim, two arrivals!
    it_data = []
    
    for t in range(NR_SIM_STEPS):
        # check new arrivals:
        check_new_arrivals(next_arrivals, queues)
        
        # check desks if one is idle or just finished a customer
        check_cash_desk(queues, rem_service_times)
        
        # print status
        if PRINT_EVERY_STEP:
            print_status(t, queues, rem_service_times)
            
        # save iteration data
        save_it_data(it_data, queues, rem_service_times)
        
        # finished iteration, decrease all times:
        for rem_time_list in rem_service_times.values():
            for i, time in enumerate(rem_time_list):
                rem_time_list[i] = time - 1 if time is not None else None
        for type, arrival in next_arrivals.items():
            next_arrivals[type] -= 1
    
    # iteration finished, print avg queue lengths
    print('Avergerage queue length before normal desks: {:.2f} customer'.format(
        it_data[-1]['cum_queue_length_normal'] / (nr_normal_desk * NR_SIM_STEPS)))
    if nr_expess_desk:
        print('Avergerage queue length before express desks: {:.2f} customer'.format(
            it_data[-1]['cum_queue_length_express'] / (nr_expess_desk * NR_SIM_STEPS)))
    return it_data

def main():
    print('Simulation having 2 Normal Desks and 0 Express Desks:')
    first = simulate_cash_desks(2, 0)
    print()
    print('Simulation having 2 Normal Desks and 1 Express Desks:')
    sec = simulate_cash_desks(2, 1)
    print()
    
    if PLOT:
        plot_simulation(first)
    
main()