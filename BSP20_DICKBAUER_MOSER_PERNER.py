"""
    BSP 20 - Instandhaltung
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""

from lib import random_std

SIMULATION = 55000
NO_OF_VACUUM_TUBES = 4
COST_SHUTDOWN_PER_HOUR = 100
COST_PER_TUBE = 20
HOURS_SHUTDOWN_ALL = 2
HOURS_SHUTDOWN_ONE = 1


def simulate_replace_all():
    print('Start simulation of replacing all tubes at failure of one:')
    vacuum_tube_list = []
    remain_hours = SIMULATION
    count_replacement = 0
    costs = 0
    
    while remain_hours >= 0:
        vacuum_tube_list = []
        # generate 4 new tubes:
        for i in range(NO_OF_VACUUM_TUBES):
            vacuum_tube_lifetime = max(random_std(1500, 500), 0)
            vacuum_tube_list.append(vacuum_tube_lifetime)
        
        print('Remaing hours: {:.2f}h'.format(remain_hours))
        print('Remaining lifetime of tubes before maintenance: {}'.format([round(elem, 2) for elem in vacuum_tube_list]))
        min_tube_lifetime = min(vacuum_tube_list)
        if min_tube_lifetime >= remain_hours:
            print('No maintenance required till the end of simulation\n')
            break
        costs_of_period = COST_SHUTDOWN_PER_HOUR * HOURS_SHUTDOWN_ALL + NO_OF_VACUUM_TUBES * COST_PER_TUBE
        costs += costs_of_period
        remain_hours -= (min_tube_lifetime + HOURS_SHUTDOWN_ALL)
        count_replacement += 1
        print('Remaining lifetime of tubes after maintenance:  {}'.format([round(elem, 2) for elem in vacuum_tube_list]))
        print('Costs of this period: {}'.format(costs_of_period))
        print()
    print('Costs of the policy of replacing all:', costs)
    print('Nr. of shutdowns: {}'.format(count_replacement))
    
def simulate_replace_one():
    print('Start simulation of replacing only the broken tube:')
    vacuum_tube_list = []
    remain_hours = SIMULATION
    count_replacement = 0
    costs = 0
    while remain_hours >= 0:
        vacuum_tube_list = []
        # generate 4 new tubes at start, and 1 in the following iteration:
        for i in range(NO_OF_VACUUM_TUBES - len(vacuum_tube_list)):
            vacuum_tube_lifetime = max(random_std(1500, 500), 0)
            vacuum_tube_list.append(vacuum_tube_lifetime)
        
        print('Remaing hours: {:.2f}h'.format(remain_hours))
        print('Remaining lifetime of tubes before maintenance: {}'.format([round(elem, 2) for elem in vacuum_tube_list]))
        index_of_minimum = vacuum_tube_list.index(min(vacuum_tube_list))
        min_tube_lifetime = vacuum_tube_list.pop(index_of_minimum)
        if min_tube_lifetime >= remain_hours:
            print('No maintenance required till the end of simulation\n')
            break
        
        # reduce all lifetimes of all tubes:
        for i in range(len(vacuum_tube_list)):
            vacuum_tube_list[i] -= min_tube_lifetime
        
        costs_of_period = COST_SHUTDOWN_PER_HOUR * HOURS_SHUTDOWN_ONE + COST_PER_TUBE
        costs += costs_of_period
        remain_hours -= (min_tube_lifetime + HOURS_SHUTDOWN_ONE)
        count_replacement += 1
        print('Remaining lifetime of tubes after maintenance:  {}'.format([round(elem, 2) for elem in vacuum_tube_list]))
        print('Costs of this period: {}'.format(costs_of_period))
        print()
    print('Costs of the policy of replacing only one:', costs)
    print('Nr. of shutdowns: {}'.format(count_replacement))
    
    
def main():
    simulate_replace_all()
    for i in range(5): print()
    simulate_replace_one()
    
main()