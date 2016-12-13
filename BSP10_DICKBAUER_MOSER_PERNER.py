"""
    BSP 10 - Mastermind
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""
DEBUG = False
OPTION = False

import sys
from lib import random_number_from_interval, user_input

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
                      # *     TRY AGAIN y/n!?    * #
                      # ************************** #
                      ##############################
""")


#INPUT:
NUMBERS = [1, 2, 3, 4, 5, 6]    #numbers used in this game
NUMBER_OF_NUMBERS = 6

def main():
    print(INTRO)
    keep_going()
    
    play_again = True
    while play_again:
        play_game()
        ask_for_replay = input()
        if ask_for_replay == 'y':
            play_again
        else:
            play_again = False
            print('                                  BYE BYE')
    
def play_game():
    number_of_rounds = user_input([
        ['Please enter the number of rounds', int, 10]], DEBUG)[0]
    
    created_code = create_code()   #given by a defined variable
    if OPTION:
        # show the right answer:
        print('Right answer would be:', created_code)
    
    for round in range(number_of_rounds):
        bet = ask_user_for_digits()
        #bet = [4, 2, 0, 0]
        print('Your bet:',bet)
        nr_right, nr_wrong = check_user_input(created_code, bet)
        print('Hint:', 'o'*nr_right,'x'*nr_wrong)
        if nr_right == len(bet):
            print('Your guess of ',bet,' equals the secret code!')
            print(WIN_MESSAGE)
            break
        elif round < number_of_rounds-1:
            print('Try again!')
        else:
            print('The secret code was:', created_code)
            print(LOOSE_MESSAGE)
    
def create_code():
    """This function creates a random 4-digit code out of the numbers 1 to 6"""    
    code = []
    for i in range(4):
        code.append(int(random_number_from_interval(1,6+1)))
    if DEBUG:
        return [4,5,4,2]
    return code
    
    
def check_user_input(right_digits, user_digits):
    """Returns two values: (nr_correct_on_pos, nr_correct_on_wrong_pos)
    i.e. nr_correct_on_pos is the number of correct values on the right pos
         nr_correct_on_wrong_pos is the --.-- on the wrong position"""
    nr_right_pos = 0
    nr_wrong_pos = 0
    right_digits_modified = right_digits[:]
    
    # check for right digits on right positions:
    for i, act_digit in enumerate(user_digits):
        if right_digits[i] == act_digit:
            nr_right_pos += 1
            # block found digits to make sure we dont count them twice on wrong pos
            right_digits_modified[i] = 'x'
    
    # check for digits on wrong pos:
    for i, act_digit in enumerate(user_digits):
        # skip those which we already marked as right pos:
        if right_digits[i] != act_digit:
            
            if act_digit in right_digits_modified:
                nr_wrong_pos += 1
                index_of_right_mod = right_digits_modified.index(act_digit)
                right_digits_modified[index_of_right_mod] = 'x'
            
    return nr_right_pos, nr_wrong_pos

def ask_user_for_digits():
    valid_input = False
    user_input = input('Please enter 4 digits: ')
    while valid_input == False:
        digits = []
        for i, char in enumerate(user_input):
            if char in '123456':
                digits.append(int(char))
            else:
                break
        if len(digits) == 4:
            valid_input = True
        else:
            user_input = input('Make sure to enter 4 integers between 1 and 6: ')
    return digits

def check_if_user_wants_to_play():
    answer = input()
    if answer == y:
        return True
    else:
        return False

def keep_going():
    if DEBUG:
        return
    answer = input("                                 y/n: ")
    if answer == "y":
        print("                               Let's play!\n")
    elif answer == "n":
        print("                                Bye, bye!")
        raise SystemExit
    else:
        answer = keep_going()

main()