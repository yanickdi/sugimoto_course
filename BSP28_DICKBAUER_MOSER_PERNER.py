"""
    BSP 28 - Monteur
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""
from lib import random_exp

NR_MACHINES = 4
EXP_REPAIR_TIME = 1
FREQUENCY = 60 # simulation steps per hour
SIM_DURATION = 10 # hour of simulation

STATE_MECHANIC_IDLE = 'coffee'
STATE_MECHANIC_REPAIRING = 'working'

STATE_MACHINE_WORKING = 0
STATE_MACHINE_WAITING = 1
STATE_MACHINE_IN_REPAIR = 2

def create_failure_free_time():
    # lambda is 1/6 --> mean is 6
    mean = 6
    time = int(random_exp(mean) * FREQUENCY)
    if time == 0:
        print('warning, time would be 0 increase simulation frequency')
        time = 1
    return time

def create_repair_time():
    # mean is 1
    mean = 1
    while True:
        time = int(random_exp(mean) * FREQUENCY)
        if time != 0:
            break
        #print('warning, time would be 0 increase simulation frequency')
        #time = 1
    return time

def simulate(nr_mechanics):
    machines = [
        {'state' : STATE_MACHINE_WORKING, 'rem_time' : create_failure_free_time()}
        for i in range(NR_MACHINES)]
    mechanics = [{'state': STATE_MECHANIC_IDLE, 'machine' : None}]
    queue_repair = []
    print('initial state', machines)
    for t in range(FREQUENCY * SIM_DURATION):
        for m in range(NR_MACHINES):
            machine = machines[m]
            
    
        for i in range(NR_MACHINES):
            machines[i]['rem_time'] -= 1
        print(machines)
        print(create_repair_time())
        

def main():
    simulate(1)
    
main()