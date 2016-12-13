"""
    BSP 12 - Urlaub
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
    Info: Markov Process
"""

from lib import create_matrix, print_matrix, loaded_random_choice

TRANS_MATRIX = [[ 0.4, 0.3, 0.2, 0.1],  #Karibik
               [0.2, 0.5, 0.2, 0.1],    #Kenia
               [0.1, 0.3, 0.3, 0.3],    #Thailand
               [0.2, 0.3, 0.1, 0.4]]    #Nepal

START_VECTOR = [100, 250, 50, 75]
FIXED_YEARS = 10
          
def main():
    next_year = START_VECTOR[:]
    theorectical = START_VECTOR[:]
    for i in range(FIXED_YEARS):
        act_year = next_year
        next_year = simulate_one_year(act_year)
        theorectical = vector_matrix_multiplication(theorectical, TRANS_MATRIX)
        diff = vector_substraction(next_year, act_year)
        diff_strings = '[' + ', '.join(['{:+d}'.format(elem) for elem in diff]) + ']'
        print('             ' + ', '.join(['Ka', 'Ke', 'Th', 'Ne']))
        print('Old Vector:', act_year)
        print('New Vector:', next_year)
        print('Difference:', diff_strings)
        print()
        
    print('Theoretical distribution after {} years: {}'.format(FIXED_YEARS,
        [round(elem, 2) for elem in theorectical]))
    
    assert sum(START_VECTOR) == sum(next_year)
    
def simulate_one_year(act_vector):
    """ Simulates one year and returns the vector of travellers next year"""
    act_vector = START_VECTOR[:]
    next_vector = [0, 0, 0, 0]
    for country in range(len(act_vector)):
        travellers = act_vector[country]
        for traveller in range(travellers):
            probability_list = TRANS_MATRIX[country]
            next_country = loaded_random_choice(probability_list)
            next_vector[next_country] += 1
    return next_vector
    
def vector_substraction(vec1, vec2):
    """Does a vector subtraction, returns a new vector where new = vec1 - vec2"""
    assert len(vec1) == len(vec2)
    new_vec = []
    for i in range(len(vec1)):
        new_vec.append(vec1[i] - vec2[i])
    return new_vec
    
def vector_matrix_multiplication(vector, matrix):
    new_vector = [0] * len(vector)
    for j in range(len(vector)):
        for i in range((len(vector))):
            new_vector[j] += (matrix[i][j] * vector[i])
    return new_vector
    
main()