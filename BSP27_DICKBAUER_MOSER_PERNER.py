"""
    BSP 27 - Epidemie
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""
from lib import user_input, create_matrix, random_choice_and_pop, loaded_random_choice

DEBUG = True

# option constants:
OPTION_INFECTION_RATE = 0
OPTION_INCUBATION_TIME = 1

INFECTION_RATE_DECREASING_VAL = .1 # start rate decreases by 10 % each step

# some status constants:
ALIVE = 1
DEAD = -1
INFECTED = 0

def create_field(size_x, size_y, initialize=True):
    """ creates an x*y matrix where each field is a dictionary that saves information about its field state"""
    field = create_matrix(size_x, size_y)
    for x in range(size_x):
        for y in range(size_y):
            if initialize:
                field[x][y] = {
                    'status' : ALIVE
                    }
            else:
                field[x][y] = None
    return field
    
def random_infect(field, nr_infections):
    """ randomly infects nr_infections units of the field
        note: doesn't check whether the unit is already infected/dead
    """
    # all point combinations are possible targets:
    pool = list(x_y_combinations(field))
    for i in range(nr_infections):
        # choose one from pool, infect the unit and remove it from the pool
        point = random_choice_and_pop(pool)
        x,y = point[0], point[1]
        infect_unit(field, point)
        
def infect_unit(field, point):
    """ Sets a point as infected and starts its time counter """
    x, y = point[0], point[1]
    unit = field[x][y]
    assert unit['status'] == ALIVE
    unit['status'] = INFECTED
    unit['infected_since'] = 0
                
def check_field_status(field):
    """ counts nr_alive, nr_infected and nr_dead units and returns a dictionary containing these values"""
    nr_alive, nr_infected, nr_dead = 0, 0, 0
    for x, y in x_y_combinations(field):
        status = field[x][y]['status']
        if   status == ALIVE: nr_alive += 1
        elif status == DEAD : nr_dead += 1
        elif status == INFECTED: nr_infected += 1
    return {'nr_alive' : nr_alive, 'nr_infected' : nr_infected, 'nr_dead' : nr_dead}
                
def simulate(size, nr_start_points, option, option_data):
    """
    The implementation of the epidemic simulation
    
    option_data: infection rate or incubation time - depends on option_data
    """
    field = create_field(size[0], size[1])
    random_infect(field, nr_start_points)
    iterations = 0
    
    # simulate until there is no living unit any more
    while check_field_status(field)['nr_alive'] > 0:
        iterations += 1
        # copy the field of the actual iteration
        next_field = copy_field(field)
        # iterate over all infected units of the actual field:
        for inf_x, inf_y in infected(field):
            for neighb_x, neighb_y in alive_neighbours(field, (inf_x,inf_y)):
                # this neighbour is a candidate, try to infect her:
                do_infect = is_contact_positive(option, option_data, field[inf_x][inf_y]['infected_since'])
                if do_infect:
                    infect_unit(field, (neighb_x, neighb_y))
                pass
            
        if iterations >= 1:
            break
            
def is_contact_positive(option, option_data, infected_since):
    """
        This function returns True if a given contact with an infected unit `unit`
        means that the neighbour unit will also be infected or not
        
        This function is a stochastic function, depending on the option and option_data
    """
    if option == OPTION_INFECTION_RATE:
        # infection rate is increasing
        infection_start_rate = option_data
        infection_rate = infection_start_rate * (1 - INFECTION_RATE_DECREASING_VAL )** infected_since
    else:
        raise NotImplementedError()
    
    probs = [infection_rate, 1 - infection_rate] # to be infected or not
    return [True, False][loaded_random_choice(probs)]
            
def alive_neighbours(field, point):
    """ Yields each alive neighbour of point - yields (x,y) """
    x, y = point[0], point[1]
    deltas = (-1, 0, 1)
    pool = [ (x+delta_x, y+delta_y) for delta_x in deltas for delta_y in deltas]
    for neighbour_x, neighbour_y in pool:
        if x == neighbour_x and y == neighbour_y: continue
        if neighbour_x < 0 or neighbour_x >= len(field): continue
        if neighbour_y < 0 or neighbour_y >= len(field[x]): continue
        yield neighbour_x, neighbour_y
    else:
        return []
    
            
def x_y_combinations(field):
    """ Returns an iterater object that yields each (x,y) combination of the field"""
    for x in range(len(field)):
        for y in range(len(field[x])):
            yield x,y
            
def infected(field):
    """ Returns an iterator object that yields each (x,y) combination of infected fields """
    for x,y in x_y_combinations(field):
        if field[x][y]['status'] == INFECTED:
            yield x,y
            
def copy_field(field):
    """ Returns a deep copy of the field matrix and returns it"""
    # not sure if copy.deepcopy(x) is allowed, so we will do it manually:
    new_field = create_field(len(field), len(field[0]), initialize=False)
    
    for x,y in x_y_combinations(field):
        unit = field[x][y]
        new_unit = {
            'status' : unit['status']}
        if unit['status'] == INFECTED:
            new_unit['infected_since'] = unit['infected_since']
        new_field[x][y] = new_unit
    return new_field

def main():
    # get user input:
    size_x, size_y, nr_start_points, option = user_input([
        ('Field size x', int, 20), 
        ('Field size y', int, 20), 
        ('Amount of start points', int, 2),
        ('Variant Decreasing injection rate [type a] or variant Incubation time [type b]', str, 'a')], DEBUG)
    if option == 'a':
        option = OPTION_INFECTION_RATE
        option_data, = user_input([
            ('You selected variant a) The injection rate decreases each period by 10%. Start rate in %', int, 50)], DEBUG)
        option_data /= 100
    else:
        option = OPTION_INCUBATION_TIME
        option_data, = user_input([
            ('You selected variant b) Incubation time', int, 4)], DEBUG)
    
    # do the simulation
    simulate([size_x, size_y], nr_start_points, option, option_data)
    
main()