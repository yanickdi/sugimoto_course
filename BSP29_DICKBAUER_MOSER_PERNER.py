"""
    BSP 29 - Bankomat
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""
from lib import random_exp, _dbg

DEBUG = False
PRINT_EVERY_STEP = DEBUG

FREQUENCY = 2 # simulation steps per minute

ATM_MAX_QUEUE_SIZE = 3
ATM_FIX_COSTS = 10000
ATM_SAVINGS_PER_CUSTOMER = .1

DAYS_PER_YEAR = 365

def generate_next_customer_arrival():
    rand = random_exp(1)
    time = int(rand * FREQUENCY)
    if time == 0:
        _dbg('warning, increase simulation frequency', DEBUG)
        time = 1
    return time
    
def generate_atm_time():
    rand = random_exp(2)
    time = int(rand * FREQUENCY)
    if time == 0:
        _dbg('warning, increase simulation frequency', DEBUG)
        time = 1
    return time
    
def check_new_arrival(next_arrival, nr_arrivals, nr_manual_served, queue_sizes):
    """ Checks if a customer arrives at the bank. If yes, try to allocate her to
        a free atm. If that is not possible it will increase nr_manual_customers.
        Returns two vals: next_arrival, nr_manual_customers
    """
    if next_arrival == 0:
        _dbg('customer arrived'.format(type), DEBUG)
        nr_arrivals += 1
        # find best queue
        q_ind, shortest_queue_size = min(enumerate(queue_sizes), key=lambda k: k[1])
        if shortest_queue_size >= 3:
            # no atm can serve the customer, increase nr_manual_customers
            nr_manual_served += 1
            _dbg('every queue too long for customer, sh** thats another 10 cent', DEBUG)
        else:
            # no problem
            queue_sizes[q_ind] += 1
        # create a new next_arrival
        next_arrival = generate_next_customer_arrival()
    return next_arrival, nr_arrivals, nr_manual_served
    
def check_machines(rem_times, queue_sizes):
    """ Checks each atm - if one is free, it will serve the next of its queue """
    for m, rem_time in enumerate(rem_times):
        # is this atm idle or just finished a customer?
        if rem_time == None or rem_time == 0:
            if rem_time == 0:
                # this customer just finished
                rem_times[m] = None
                _dbg('customer finished on atm {}'.format(m+1), DEBUG)
            if queue_sizes[m] > 0:
                # serve the next customer
                queue_sizes[m] -= 1
                rem_times[m] = generate_atm_time()
                
def print_status(t, queue_sizes, rem_times, next_arrival, nr_arrivals, nr_manual_served):
    print('Iteration :{}'.format(t))
    for atm in range(len(queue_sizes)):
        queue_size = queue_sizes[atm]
        rem_time = rem_times[atm]
        rem_time_str = 'no customer' if rem_time is None else str(rem_time)
        print('  atm #{}'.format(atm+1))
        print('     queue length: {}'.format(queue_size))
        print('     rem_time of actual customer on atm: {}'.format(rem_time_str))
    print('  Next customer arrives in: {}'.format(next_arrival))
    print('  Nr. ATM served:    {}'.format(nr_arrivals - nr_manual_served))
    print('  Nr. manual served: {}'.format(nr_manual_served))
    print()

def simulate_day(nr_atms):
    queue_sizes = [0 for i in range(nr_atms)]
    rem_times = [None for i in range(nr_atms)]
    nr_arrivals, nr_manual_served = 0, 0
    next_arrival = 0
    
    # simulate an hour
    for t in range(int(FREQUENCY * 60 * 15)):
        # check new arrival:
        __ret = check_new_arrival(next_arrival, nr_arrivals, nr_manual_served, queue_sizes)
        next_arrival, nr_arrivals, nr_manual_served = __ret
        # check machines
        check_machines(rem_times, queue_sizes)
        
        # print status
        if PRINT_EVERY_STEP:
            print_status(t, queue_sizes, rem_times, next_arrival, nr_arrivals, nr_manual_served)
        
        # decrease all times
        for i, rem_time in enumerate(rem_times):
            rem_times[i] = rem_time - 1 if rem_time is not None else None
        next_arrival -= 1
    return nr_arrivals, nr_manual_served
        
def calc_savings_in_a_year(nr_atms):
    nr_arrivals, nr_manual_served = simulate_day(nr_atms)
    nr_arrivals, nr_manual_served
    nr_atm_served = nr_arrivals - nr_manual_served
    
    # project the simulated day to a year:
    nr_arrivals, nr_manual_served, nr_atm_served = nr_arrivals * DAYS_PER_YEAR, nr_manual_served * DAYS_PER_YEAR, nr_atm_served * DAYS_PER_YEAR
    savings = nr_atm_served * ATM_SAVINGS_PER_CUSTOMER
    invested = nr_atms * ATM_FIX_COSTS
    payoff_time = invested / savings
    
    print('Simulated a year having {} atm\'s'.format(nr_atms))
    print(' Total number of customers arrived: {}'.format(nr_arrivals))
    print(' Number of customers on atm machines: {}'.format(nr_atm_served))
    print(' Number of manual served customers  : {}'.format(nr_manual_served))
    print(' Savings: {:.2f} EUR'.format(savings))
    print(' Invested: {} EUR'.format(invested))
    print(' Payoff time: {:.2f} years'.format(payoff_time))

def main():
    calc_savings_in_a_year(1)
    print()
    calc_savings_in_a_year(2)
    print()
    calc_savings_in_a_year(3)
    
main()