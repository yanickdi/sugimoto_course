"""
    BSP 03 - Sortierung von Zufallszahlen
    Dickbauer Yanick 1030489, Patrick Moser 1114954, Perner Manuel 0633155
    WS 2016
"""
# INPUT:
NUMBER_OF_POINTS = 10
X_MAX = 20
Y_MAX = 30


from lib import random_number_from_interval

def sort_key_function(input):
    # sort according to the points x value -> if its the same, according to the y value
    return (input[0], input[1])

def main():
    # generate points:
    point_list = []
    for i in range(NUMBER_OF_POINTS):
        point_x = random_number_from_interval(1, X_MAX)
        point_y = random_number_from_interval(1, Y_MAX)
        point = (point_x, point_y)
        point_list.append(point)
        
    # sort
    sorted_point_list = sorted(point_list, key=sort_key_function)
    
    # output
    for x, y in sorted_point_list:
        print('x: {:5f}\ty: {:5f}'.format(round(x, 2), round(y, 2)))
        

main()
