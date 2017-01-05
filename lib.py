import random
from math import sin, log, pi

def random_number_from_interval(lower, upper):
    """Returns a random number out of the interval (lower, upper["""
    val = random.random()
    return lower + (upper -lower) * val
    
def random_std(mean=0, sigma=1):
    """Returns a normally distrubed random number"""
    # create two random numbers [0,1(
    u1, u2 = random.random(), random.random()
    zz = (-2 * log(u1))**(1/2) * sin(2 * pi * u2)
    return sigma * zz + mean

def random_choice(choices):
    """This function takes a list of choices and randomly picks one out of it and returns the element"""
    number_of_elements = len(choices)
    random_position = int(random_number_from_interval(0, number_of_elements))
    return choices[random_position]
    
    
def loaded_random_choice(probability_list):
    """This stochastic function takes a list as input and returns a random index corresponding to the list.
    The randomness of the index is loaded: the probality of choosing an index is exactly the corresponding
    probability given at this index position of the input list.
    e.g.: [0.2, 0.8] --> the return value of `0` is 20% likely, the return value of `1` is 80% likely
    note that the sum of all values in the `probability_list` has to be 1
    """
    n = len(probability_list)
    random_number = random.random()
    cum_p = 0
    for i in range(n):
        cum_p += probability_list[i]
        if cum_p > random_number:
            return i
    return None
    
def create_matrix(m, n, default_value=None):
    """Returns a mxn list of lists, where each value is None or default param"""
    matrix = [[default_value for j in range(n)]for i in range(m)]
    matrix = []
    for row in range(m):
        line_list = []
        for col in range(n):
            line_list.append(default_value)
        matrix.append(line_list)
    return matrix
    
def euclidean_distance(point_1, point_2):
    """
        Calculates the euclidean distance between two points
        
        point_1: a tuple of (x,y) values
        point_2: a tuple of (x,y) values
    """
    delta_x = point_2[0] - point_1[0]
    delta_y = point_2[1] - point_1[1]
    return (delta_x ** 2 + delta_y ** 2) ** 0.5
    
    
def print_matrix(matrix, ndigits_round=2):
    """Prints a list of lists of floats beautiful to stdout. """
    for line in matrix:
        print(''.join(['{:7}'.format(round(elem, ndigits_round)) for elem in line]))
        
        
def user_input(input_vars, use_defaults=False):
    """
        This function returns a tuple of values, given by the user_input
        
        input_vars : a tuple of tuples, each inner tuple must have 3 values:
                        (text, type, default_value)
                     e.g.
                        ('How old are you', int, 20)             
    """
    if use_defaults:
        return tuple(elem[2] for elem in input_vars)
    
    values = []
    for elem in input_vars:
        valid = False
        while not valid:
            try:
                inp_val = input('{} [default is {}]: '.format(elem[0], elem[2]))
                if inp_val == '':
                    inp_val = str(elem[2])
                type = elem[1]
                if type == int:
                    inp_val = int(inp_val)
                elif type == float:
                    inp_val = float(inp_val)
                valid = True
            except ValueError:
                print(inp_val, 'is not valid, please try again')
        values.append(inp_val)
    return tuple(values)