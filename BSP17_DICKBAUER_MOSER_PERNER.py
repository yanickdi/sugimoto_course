"""
    BSP 17 - Warteschlangenmodell
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""

from lib import user_input, loaded_random_choice

DEBUG = False
PLOT = False
P = 0.5
Q = 0.5

def plot(customer_waiting):
    import matplotlib.pyplot as plt
    plt.plot(customer_waiting, label='Queue length')
    plt.show()


def main():
    customer_waiting = []
    customer_arrivals = []
    customer_served = []
    waiting = 0
    arrivals = [(1-P), P]
    servings = [(1-Q), Q]
    simulation_duration = user_input((
        ('Number of simulations', int, 100), ),DEBUG)[0]
    for i in range(simulation_duration):
        print('Queue length at beginning of period {}: {}'.format(i+1, waiting))
        old_waiting = waiting
        arrived = loaded_random_choice(arrivals)
        served = loaded_random_choice(servings)
        if arrived == 1:
            waiting += 1
        if served == 1 and waiting >= 1:
            waiting -= 1
            customer_served.append(1)
        else:
            customer_served.append(0)
        customer_waiting.append(waiting)
        customer_arrivals.append(arrived)
        print('Queue length at end of period {}: {}'.format(i, waiting))
        print('Change in Queue length {}: {}\n'.format(i, waiting-old_waiting))
    
    avg_waiting_time = sum(customer_waiting)/sum(customer_arrivals)
    utilization = sum(customer_served)/simulation_duration
    avg_queue_length = sum(customer_waiting)/simulation_duration
    print('Average Waiting Time: {:.2f}'.format(avg_waiting_time))
    print('Utilization: {:.2f}'.format(utilization))
    print('Average Queue Length: {:.2f}'.format(avg_queue_length))
    
    if PLOT:
        plot(customer_waiting)

main()

