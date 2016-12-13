"""
    BSP 12 VACATION - Markov Process
    Dickbauer Yanick 1030489, Patrick Moser 1114954, Perner Manuel 0633155
    WS 2016
"""

from lib import create_matrix, print_matrix

trans_matrix = [[ 0.4, 0.3, 0.2, 0.1],  #Karibik
               [0.2, 0.5, 0.2, 0.1],    #Kenia
               [0.1, 0.3, 0.3, 0.3],    #Thailand
               [0.2, 0.3, 0.1, 0.4]]    #Nepal
          
 
print_matrix(matrix, ndigits_round=2)

main()