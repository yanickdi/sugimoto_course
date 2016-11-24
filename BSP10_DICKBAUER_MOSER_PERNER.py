"""
    BSP10 - Mastermind
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""

from lib import random_number_from_interval

#INPUT:

NUMBER_OF_ROUNDS = 10
NUMBER_OF_TIPS = 4
NUMBERS = [1, 2, 3, 4, 5, 6]    #numbers used in this game
NUMBER_OF_NUMBERS = 6   #TODO for code testing only 

#def main():
    #pass
    

def create_code(NUMBER_OF_NUMBERS):
    code = []
    for i in range(5):
        code.append('1')
    return code
    print(code)


create_code(NUMBER_OF_NUMBERS)
#main()