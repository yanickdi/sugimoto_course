"""
    BSP10 - Mastermind
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""

from lib import random_number_from_interval

INTRO = ("""
================================================================================
################################################################################
================================================================================
########  x   x     x      xxxx xxxxx xxxxx xxxx  x   x xxx x   x xxx  #########
########  xx xx    x x    x       x   x     x   x xx xx  x  xx  x x  x  ########
########  x x x   xxxxx   xxxxx   x   xxxx  xxxx  x x x  x  x x x x   x  #######
########  x   x  x     x      x   x   x     x  x  x   x  x  x  xx x  x  ########
########  x   x x       x xxxx    x   xxxxx x   x x   x xxx x   x xxx  #########
================================================================================
################################################################################
================================================================================

This is a little mastermind-game implemented in python3!

Instructions:
The user plays against the computer.

The computer randomly creates a 4-digit secret code, which the user has to 
guess.
You will be asked to enter a 4-digit bet with integer values between 1 and 6.

The computer will give you hints about your guess.

                          Are you ready to play?
            (Enter y, if you are ready to play, or n to quit.)
""")

WIN_MESSAGE = ("""
                      ##############################
                      # ************************** #
                      # *        SUCCESS!        * #
                      # * ---------------------- * #
                      # *    YOU ARE GENIUS!     * #
                      # * YOU  CRACKED THE CODE! * #
                      # ************************** #
                      ##############################
""")

LOOSE_MESSAGE = ("""
                      ##############################
                      # ************************** #
                      # *       YOU LOOSE!       * #
                      # * ---------------------- * #
                      # * YOU RAN OUT OF ROUNDS. * #
                      # *      TRY AGAIN!?       * #
                      # ************************** #
                      ##############################
""")


#INPUT:
NUMBER_OF_ROUNDS = 10
NUMBERS = [1, 2, 3, 4, 5, 6]    #numbers used in this game
NUMBER_OF_NUMBERS = 6   #TODO for code testing only 

def main():
    print(INTRO)
    
    answer = keep_going()
    #created_code = create_code()   #given by a defined variable
    created_code = [4,5,3,2]    #to be replaced by random code for gaming
    #for i in range(NUMBER_OF_ROUNDS):

    bet = ask_user_for_digits()
    #bet = [4, 2, 0, 0]
    print('Your bet:',bet)
    nr_right, nr_wrong = check_user_input(created_code, bet)
    print('Hint:', 'o'*nr_right,'x'*nr_wrong)
    if nr_right == len(bet):
        print('Your guess of ,',bet,' equals the secret code!')
        print(WIN_MESSAGE)
    else: 
        print('fuck')
    
def create_code():
    """This function creates a random 4-digit code out of the numbers 1 to 6"""    
    code = []
    for i in range(4):
        code.append(int(random_number_from_interval(1,6+1)))
    return code
    #print(code)
    
    
def check_user_input(right_digits, user_digits):
    """Returns two values: (nr_correct_on_pos, nr_correct_on_wrong_pos)
    i.e. nr_correct_on_pos is the number of correct values on the right pos
         nr_correct_on_wrong_pos is the --.-- on the wrong position"""
    nr_right_pos = 0
    nr_wrong_pos = 0
    assert len(right_digits) == len(user_digits)
    for i in range(len(user_digits)):
        act_digit = user_digits[i]
        if act_digit == right_digits[i]:
            # this digit is on the right position!
            nr_right_pos += 1
        elif act_digit in right_digits:
            # this digit is not on the right position,
            # but at least it is part of the right digits
            nr_wrong_pos += 1
    return nr_right_pos, nr_wrong_pos

def check_for_break():
    print('Abbruchkriterien programmieren!')    #Abbruch nach einer bestimmten Anzahl an Runden/NUMBER_OF_ROUNDS

def ask_user_for_digits():
    digits = []
    for i in range(4):
        digit = int(input('Please enter digit #{}: '.format(i+1)))
        digits.append(digit)
        print(digits)
    return digits

def check_if_user_wants_to_play():
    answer = input()
    if answer == y:
        return True
    else:
        return False

def keep_going():
    answer = input("                                 y/n: ")
    if answer == "y":
        print("                               Let's play!\n")
    elif answer == "n":
        print("                                Bye, bye!")
        raise SystemExit
    else:
        answer = keep_going()

main()