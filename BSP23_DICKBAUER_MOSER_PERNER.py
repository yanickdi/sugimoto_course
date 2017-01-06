"""
    BSP 23 - Fertigungsstrasse
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""
import sys
from lib import loaded_random_choice


PRINT_EVERY_STEP = False

NO_MACHINES = 3
NORMAL_PROCESSING_TIME_PER_MACHINE = 1 # minute per machine
LONG_PROCESSING_TIME_PER_MACHINE = 5 # minutes
FAULTY_PART_RATIO = 0.15 # probabilty of having a faulty product that takes more time on each machine

SIMULATION = 180 #minutes


class Product:
    def __init__(self, id):
        self.id = id
        if loaded_random_choice([FAULTY_PART_RATIO, 1 - FAULTY_PART_RATIO]) == 0:
           # this product is faulty:
           self.time_per_machine = LONG_PROCESSING_TIME_PER_MACHINE
        else:
           self.time_per_machine = NORMAL_PROCESSING_TIME_PER_MACHINE
        self.remaining_t_on_m = self.time_per_machine

def simulate_assembly_line(minutes, nr_machines, buffer_size, print_every_step=True):
    nr_jobs_created = 0
    nr_jobs_finished = 0
    simulation_iteration_data = []
    
    # create buffers (empty queues) before each machines:
    buffers = [[] for i in range(nr_machines)]
    # create empty processing lists for each machine:
    machines_act_job = [None for i in range(nr_machines)]
    
    def _check_before_machine(act_machine_nr):
        """ helper function:
            if there is no job on this machine, it checks if it can take one from before
        """
        assert machines_act_job[act_machine_nr] == None
        nonlocal nr_jobs_created
        # no job on this machine, are we at the first machine?
        if act_machine_nr == 0:
            # we can create a new job and process it on this machine
            machines_act_job[0] = Product(nr_jobs_created)
            nr_jobs_created += 1
        # is there a job on the queue before?
        elif len(buffers[act_machine_nr]) > 0:
            # move the first job out of the queue onto this machine
            machines_act_job[act_machine_nr] = buffers[act_machine_nr].pop(0)
    
    #start simulation:
    for t in range(SIMULATION):
        # we have to go from the last machine to the first:
        for act_machine_nr in reversed(range(nr_machines)):
            #is there a job on that machine?
            if machines_act_job[act_machine_nr] == None:
                _check_before_machine(act_machine_nr)
            else:
                # there is a job on this machine, reduce its remaining time
                act_job = machines_act_job[act_machine_nr]
                act_job.remaining_t_on_m -= 1
                if act_job.remaining_t_on_m <= 0:
                    # job is done - move it further
                    next_machine_nr = act_machine_nr + 1
                    if next_machine_nr == nr_machines:
                        # job finished the system
                        nr_jobs_finished += 1
                        machines_act_job[act_machine_nr] = None
                    else:
                        # move it to the next machine if possible
                        if machines_act_job[next_machine_nr] == None:
                            machines_act_job[next_machine_nr] = act_job
                            act_job.remaining_t_on_m = act_job.time_per_machine
                            machines_act_job[act_machine_nr] = None
                            _check_before_machine(act_machine_nr)
                        else:
                            # next machine not free - move it to the queue
                            if len(buffers[next_machine_nr]) >= buffer_size:
                                # buffer is full already, set its remaining time to -1
                                act_job.remaining_t_on_m = -1
                            else:
                                # ok, we can move it to the queue
                                buffers[next_machine_nr].append(act_job)
                                act_job.remaining_t_on_m = act_job.time_per_machine
                                machines_act_job[act_machine_nr] = None
                                
        # save some data of this iteration to simulation_iteration_data for evaluation later
        simulation_iteration_data.append(
            {'machine_is_processing' : [machines_act_job[i] is not None and machines_act_job[i].remaining_t_on_m >= 0 for i in range(nr_machines)],
            'machine_is_idle' : [machines_act_job[i] is None or machines_act_job[i].remaining_t_on_m < 0 for i in range(nr_machines)],
            'queue_length' : [len(buffers[i]) for i in range(nr_machines)]
        })
        
        if print_every_step:
            print('t={}'.format(t))
            for i in range(nr_machines):
                job_on_machine = machines_act_job[i]
                queue_before = buffers[i]
                print('  Machine #{}:'.format(i+1))
                print('    Job id on machine: {} - remaining time on machine: {}'.format(
                    job_on_machine.id if job_on_machine is not None else '-',
                    job_on_machine.remaining_t_on_m if job_on_machine is not None else '-'))
                print('    Jobs in queue before: {}'.format([job.id for job in queue_before]))
            print('\n')
            
    # evaluation
    print('Number of Jobs finished: ', nr_jobs_finished)
    for i in range(nr_machines):
        utilization_machine = sum(it['machine_is_processing'][i] for it in simulation_iteration_data) / len(simulation_iteration_data)
        cum_idle_time = sum(it['machine_is_idle'][i] for it in simulation_iteration_data)
        avg_queue_length = sum(it['queue_length'][i] for it in simulation_iteration_data) / len(simulation_iteration_data)
        print('Utilization of machine {}: {:.2f}%'.format(i, utilization_machine*100))
        print('Cumulated idle time of machine {}: {} seconds'.format(i+1, cum_idle_time))
        print('Average queue length before machine {}: {:.3f}'.format(i, avg_queue_length))
        print()


def main ():
    print('Simulation without buffer between machines: ')
    simulate_assembly_line(SIMULATION, NO_MACHINES, buffer_size=0, print_every_step=PRINT_EVERY_STEP)
    print('\n')
    print('Simulation with unlimited buffer between machines: ')
    simulate_assembly_line(SIMULATION, NO_MACHINES, buffer_size=sys.maxsize, print_every_step=PRINT_EVERY_STEP)

main()