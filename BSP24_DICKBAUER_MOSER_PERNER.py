"""
    BSP 24 - Waschstrasse
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""
from lib import random_exp, random_poisson

SHOW_PLOT = False # matplotlib must be installed!

SIM_FREQUENCY = 1 # in minutes
SIMULATIONS = 100

def plot(sim_list):
    import matplotlib.pyplot as plt
    try: import seaborn
    except: pass
    import numpy as np
    
    for (ratio_rejected, max_queue_length) in sim_list:
        ratios = np.array(ratio_rejected) * 100
        plt.plot(ratios, label='Queue Length = {}'.format(max_queue_length))
    plt.title('Rejection Rates')
    plt.xlabel('Iterations [{} per Minute]'.format(SIM_FREQUENCY))
    plt.ylabel('Ratios [%]')
    plt.ylim([-5, 60])
    plt.legend()
    plt.show()

def simulation(max_queue_length):
    next_arrival = 0
    remaining_time_in_machine = 0
    is_machine_busy = False
    num_departures = 0
    num_arrivals = 0
    num_rejected = 0
    queue_length = 0
    ratios_rejected = []
    
    for i in range(SIMULATIONS):
        # part 1: check machine:
        if remaining_time_in_machine == 0 and is_machine_busy:
            is_machine_busy = False
            num_departures += 1   # car is finished
            # machine is free, is a car waiting?
            if queue_length > 0:
                # send to machine:
                remaining_time_in_machine = create_processing_time()
                is_machine_busy = True
                queue_length -= 1
            
        # part 2: check new arrivals:
        if next_arrival == 0:
            # new customer arrives 
            num_arrivals += 1
            if not is_machine_busy:
                # machine is free, send car in
                remaining_time_in_machine = create_processing_time()
                is_machine_busy = True
            else:
                # machine is not finished yet
                # put car into the queue (if queue is not full)
                if queue_length < max_queue_length:
                    # put into queue
                    queue_length += 1
                else:
                    # reject, queue is full
                    num_rejected += 1
            # create a next arrival time:
            next_arrival = create_arrival_time()
        
        print('It {}: queue_length: {}, next_arrival: {}, rem_time_mach: {}, arrivals: {}, departures: {}, rejected: {}'.format(
            i, queue_length, next_arrival, remaining_time_in_machine, num_arrivals, num_departures, num_rejected))
        ratios_rejected.append(num_rejected / num_arrivals)
        
        # part 3: decrease all time variables
        next_arrival -= 1
        remaining_time_in_machine -= 1
    
    #simulation finished, calc ratio of rejected compared with arrivals:
    ratio_rejected = num_rejected / num_arrivals
    print('Sum of rejected: {}, Sum of arrived: {}, Rejection Ratio: {:.2f}%\n'.format(
        num_rejected, num_arrivals, ratio_rejected * 100))
    return ratios_rejected, max_queue_length

def create_processing_time():
    # the processing time is exponential distributed with an exp val of 3 min.
    p_time = int(round(random_exp(3) * SIM_FREQUENCY, 0))
    if p_time == 0:
        p_time = 1
        print('Warning: processing time would be zero, increase simulation frequency!')
    return p_time

def create_arrival_time():
    # the next customer arrives after an average time of 4 minutes
    arr_time = int(round(random_poisson(4) * SIM_FREQUENCY, 0))  # (poisson distributed)
    if arr_time == 0:
        arr_time = 1
        print('Warning: arr_time would be zero, increase simulation frequency!')
    return arr_time
    
    
def main():
    data = [
        simulation(0),
        simulation(2),
        simulation(4)]
    
    if SHOW_PLOT:
        plot(data)
    
main()