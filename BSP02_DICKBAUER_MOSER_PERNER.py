"""
    BSP 02 - Simulation von Distanzen
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""
DEBUG = False


from lib import random_number_from_interval, create_matrix,\
                euclidean_distance, print_matrix, user_input

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
    # input
    inp = user_input((
        ('Number of points', int, 10),
        ('Xmax', float, 20.0),
        ('Ymax', float, 30)), DEBUG)
    number_of_points, x_max, y_max = inp[0], inp[1], inp[2]
    
    # generate points:
    point_list = []
    for i in range(number_of_points):
        point_x = random_number_from_interval(1, x_max)
        point_y = random_number_from_interval(1, y_max)
        point = (point_x, point_y)
        point_list.append(point)
    print('Generated points: ')
    str_point_list = ','.join(('({:.2f}/{:.2f})'.format(point[0], point[1])) for point in point_list)
    print(str_point_list, '\n\nDistance Matrix:')
    
    # calculate distance matrix
    dist_matrix = calculate_distance_matrix(point_list)
    
    # print the calculated matrix
    print_matrix(dist_matrix)
        
main()