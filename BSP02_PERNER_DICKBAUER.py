"""
    BSP 02 - Simulationen von Distanzen
    Dickbauer Yanick 1030489, Perner Manuel 0633155
    WS 2016
"""
# INPUT:
NUMBER_OF_POINTS = 10
X_MAX = 20
Y_MAX = 30


from lib import random_number_from_interval, calculate_distance_matrix, print_matrix

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