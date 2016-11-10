"""
    BSP 02 - Simulationen von Distanzen
    Dickbauer Yanick 1030489, Patrick Moser 1114954, Perner Manuel 0633155
    WS 2016
"""
# INPUT:
NUMBER_OF_POINTS = 10
X_MAX = 20
Y_MAX = 30


from lib import random_number_from_interval, create_matrix, euclidean_distance, print_matrix

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

def main():
    # generate points:
    point_list = []
    for i in range(NUMBER_OF_POINTS):
        point_x = random_number_from_interval(1, X_MAX)
        point_y = random_number_from_interval(1, Y_MAX)
        point = (point_x, point_y)
        point_list.append(point)
    
    # calculate distance matrix
    dist_matrix = calculate_distance_matrix(point_list)
    
    # print the calculated matrix
    print_matrix(dist_matrix)
        
main()