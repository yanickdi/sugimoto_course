import random

def random_number_from_interval(lower, upper):
    """Returns a random number out of the interval (lower, upper["""
    val = random.random()
    return lower + (upper -lower) * val

def random_choice(choices):
    """This function takes a list of choices and randomly picks one out of it and returns the element"""
    number_of_elements = len(choices)
    random_position = int(random_number_from_interval(0, number_of_elements))
    return choices[random_position]
    
    
def loaded_random_choice(probability_list):
    """This stochastic function takes a list as input and returns a random index corresponding to the list.
    The randomness of the index is loaded: the probality of choosing an index is exactly the corresponding
    probability given at this index position of the input lix.
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