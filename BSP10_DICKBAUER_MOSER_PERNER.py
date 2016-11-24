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

def main():
    print()
    #created_code = create_code()
    created_code = [4,5,3,2]
    #for i in range(NUMBER_OF_ROUNDS):
    bet = ask_user_for_digits()
    print(bet)
    
        #bet = [4, 5, 3, 2]
        #print(created_code)
        #if created_code == bet:
         #   print('yay')
        #else: 
         #   print('fuck')
    
def create_code():
    """This function creates a random 4-digit code with out of the numbers 1 to 6"""    
    code = []
    for i in range(4):
        code.append(int(random_number_from_interval(1,6+1)))
    return code
    #print(code)

def check_for_break():
    print('Abbruchkriterien programmieren!')

def ask_user_for_digits():
    digits = []
    for i in range(4):
        digit = int(input('Please enter digit #{}: '.format(i+1)))
        digits.append(digit)
    return digits


main()