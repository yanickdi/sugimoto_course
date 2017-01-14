"""
    BSP 27 - Epidemie
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""
from lib import user_input, create_matrix

DEBUG = True

# option constants:
OPTION_INFECTION_RATE = 0
OPTION_

# some status constants:
ALIVE = 1
DEAD = -1
INFECTED = 0

def create_field(size_x, size_y):
    """ creates an x*y matrix where each field is a dictionary that saves information about its field state"""
    field = create_matrix(size_x, size_y)
    for x in range(len(size_x)):
        for y in range(len(size_y)):
            field[x][y] = {
                'status' : ALIVE
                }
                
def check_field_status(field):
    """ counts nr_alive, nr_infected and nr_dead units and returns a dictionary containing these values"""
    nr_alive, nr_infected, nr_dead = 0
    for x in range(len(size_x)):
        for y in range(len(size_y)):
            status = field[x][y]['status']
            if   status == ALIVE: nr_alive += 1
            elif status == DEAD : nr_dead += 1
            elif status == INFECTED: nr_infected += 1
    return {'nr_alive' : nr_alive, 'nr_infected' : nr_infected, 'nr_dead' : nr_dead}
                
def simulate(size, option, option_data):
    """
    The implementation of the epidemic simulation
    
    option_data: infection rate or incubation time - depends on option_data
    """
    while
    

def main():
    # get user input:
    size_x, size_y, option = user_input([
        ('Field size x', int, 20), 
        ('Field size y', int, 20), 
        ('Variant Decreasing injection rate [type a] or variant Incubation time [type b]', str, 'a')], DEBUG)
    if option == 'a':
        start_rate, = user_input([
            ('You selected variant a) The injection rate decreases each period by 10%. Start rate in %', int, 50)], DEBUG)
    else:
        inc_time, = user_input([
            ('You selected variant b) Incubation time', int, 4)], DEBUG)
    
main()