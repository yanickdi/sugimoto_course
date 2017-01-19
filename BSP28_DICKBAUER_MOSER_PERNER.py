"""
    BSP 28 - Monteur
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""
from lib import random_exp, user_input

NR_MACHINES = 4
FREQUENCY = 10 # simulation steps per hour
SIM_DURATION = 1000 # hour of simulation


STATE_MECHANIC_IDLE = 'drinking coffee'
STATE_MECHANIC_REPAIRING = 'repairing'

STATE_MACHINE_WORKING = 'working'
STATE_MACHINE_WAITING = 'waiting for repair'
STATE_MACHINE_IN_REPAIR = 'in repair'

PRINT_EVERY_STEP = False
SHOW_PLOT = True

def create_failure_free_time():
    # lambda is 1/6 --> mean is 6
    mean = 6
    time = int(random_exp(mean) * FREQUENCY)
    if time == 0:
        #print('warning, time would be 0 increase simulation frequency')
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

def working_machines(machines):
    for m, machine in enumerate(machines):
        if machine['state'] == STATE_MACHINE_WORKING:
            yield m, machines[m]
    return []

def evaluate_iteration(t, machines, mechanics, queue):
    nr_machines_in_repair = 0
    _print_step('Iteration: {}'.format(t))
    for m, machine in enumerate(machines):
        _print_step('  Machine {}: state: {}, rem_time: {}'.format(
                m+1, machine['state'], machine['rem_time']))
    _print_step()
    for m, mechanic in enumerate(mechanics):
        if mechanic['state'] == STATE_MECHANIC_REPAIRING:
            machine_nr = machines.index(mechanic['machine'])
            work_str = ', works on machine: {}'.format(machine_nr+1)
            nr_machines_in_repair += 1
        else:
            work_str = ''
        _print_step('  Mechanic {}: state: {}{}'.format(
            m+1, mechanic['state'], work_str))
    _print_step()
    _print_step('  Machines waiting for repair: {}'.format(
        [machines.index(m)+1 for m in queue]))
    _print_step('\n')
    
    return {
        'nr_machines_working' : len(list(working_machines(machines))),
        'nr_machines_in_repair' : nr_machines_in_repair,
        'nr_machines_waiting' : len(queue)
    }

def _print_step(str=''):
    if PRINT_EVERY_STEP:
        print(str)
        
        
def simulate(nr_mechanics):
    machines = [
        {'state' : STATE_MACHINE_WORKING, 'rem_time' : create_failure_free_time(),
        'id' : i}
        for i in range(NR_MACHINES)]
    mechanics = [{'state': STATE_MECHANIC_IDLE, 'machine' : None}
                    for i in range(nr_mechanics)]
    queue = []
    it_data = []
    for t in range(FREQUENCY * SIM_DURATION):
        # the machine part
        for m, machine in working_machines(machines):
            if machine['rem_time'] == 0:
                machine['state'] = STATE_MACHINE_WAITING
                queue.append(machine) # maybe a bug: state_waiting?
        # mechanics part:
        for m, mechanic in enumerate(mechanics):
            if mechanic['state'] == STATE_MECHANIC_REPAIRING:
                machine = mechanic['machine']
                # maybe she fixed the machine:
                if machine['rem_time'] == 0:
                    machine['rem_time'] = create_failure_free_time()
                    machine['state'] = STATE_MACHINE_WORKING
                    mechanic['state'] = STATE_MECHANIC_IDLE
            if mechanic['state'] == STATE_MECHANIC_IDLE:
                # check if machine is in queue
                if len(queue) > 0:
                    machine = queue.pop(0)
                    machine['state'] = STATE_MACHINE_IN_REPAIR
                    machine['rem_time'] = create_repair_time()
                    mechanic['state'] = STATE_MECHANIC_REPAIRING
                    mechanic['machine'] = machine
        
        # print actual state:
        it_data.append(evaluate_iteration(t, machines, mechanics, queue))
        
        for m, machine in enumerate(machines):
            machine['rem_time'] -= 1
    
    # evaluation
    n = len(it_data)
    
    #utilization_mechanics = sum([it['nr_machines_in_repair']/nr_mechanics for it in it_data])
    #avg_utilization_mecha
    #print(utilization_mechanics)
    return it_data

def costs(it_data, nr_mechanics, cost_downtime, labor_costs):
    #mechanics costs:
    print('Sum of labor costs with {} mechnics:'.format(nr_mechanics),SIM_DURATION * nr_mechanics * labor_costs)
    downtime = sum(NR_MACHINES - it['nr_machines_working'] for it in it_data) / FREQUENCY
    print('Sum of downtime costs with {} mechanics:'.format(nr_mechanics) ,downtime * cost_downtime)
    total_costs = (SIM_DURATION * nr_mechanics * labor_costs) + (downtime * cost_downtime)
    print('Total costs with {} mechanics:'.format(nr_mechanics), total_costs)
    

def plot(sim_data):
    import matplotlib.pyplot as plt
    import seaborn
    
    n = len(sim_data[0]['data'])
    x_vals = range(n)
    
    for it_nr, sim in enumerate(sim_data):
        nr_mechanics = sim['nr_mechanics']
        data = sim['data']
        workings = [it['nr_machines_working'] for it in data]
        cum_utilization_w = [sum(workings[0:i]) / (i * NR_MACHINES) for i in range(1,n)]
        plt.plot(x_vals[1:], cum_utilization_w, label='Avg. Machine Utilization sim {}'.format(nr_mechanics))
        
        repairs = [it['nr_machines_in_repair'] for it in data]
        cum_utilization_r = [sum(repairs[0:i]) / (i * nr_mechanics) for i in range(1,n)]
        plt.plot(x_vals[1:], cum_utilization_r, label='Avg. Mechanics Utilization sim {}'.format(nr_mechanics))
    plt.legend()
    plt.show()
    

def main():
    cost_downtime, labor_costs = user_input([('Define the downtime costs per hour', int, 1000), ('Define the labor costs per hour of the mechanics', int, 50)])
    data_sim_1 = simulate(1)
    data_sim_2 = simulate(2)
    costs(data_sim_1, 1, cost_downtime, labor_costs)
    costs(data_sim_2, 2, cost_downtime, labor_costs)
    if SHOW_PLOT:
        plot([{'nr_mechanics' : 1, 'data' : data_sim_1}, {'nr_mechanics': 2, 'data': data_sim_2}])
    
main()