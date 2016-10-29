import random

def random_number_from_interval(lower, upper):
    """Returns a random number out of the interval [lower, upper]"""
    val = random.random()
    return lower + (upper -lower) * val
    
def calculate_distance_matrix(point_list):
    """ Returns a nxn matrix (list of lists) where n is the length of the point_list
    
    point_list: Is a list of (x,y) tuples (x and y can be floating point values or integers)
    Return: Distance matrix, where d_ij is the calculated euclidean distance from point i to point j
    """
    n = len(point_list)
    matrix = create_matrix(n, n, default_value = 0.0)
    for i in range(n):
        for j in range(n):
            matrix[i][j] = euclidean_distance(point_list[i], point_list[j])
    return matrix
    
def create_matrix(n, m, default_value=None):
    """Returns a nxm list of lists, where each value is None or default param"""
    matrix = [[default_value for j in range(n)]for i in range(m)]
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