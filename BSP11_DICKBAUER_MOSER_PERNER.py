"""
    BSP11 - Schere-Stein-Papier
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""

from lib import user_input, random_number_from_interval

DEBUG = False

#INPUT:
OPTIONS = ['rock', 'paper', 'scissors']

OPTION_ROCK = 0
OPTION_PAPER = 1
OPTION_SCISSORS = 2

CPU = 0
USER = 1
DRAW = 2

ROUND_MSG = ['CPU won the round', 'You won the round', 'Round was draw']

def main():
    win_score = user_input([['Please enter the score to win the game', int, 3]], DEBUG)[0]
    
    scores = [0, 0]
    while max(scores) < win_score:
        cpu = choice_cpu()
        user = choice_user()
        round_winner = compare(cpu, user)
        if round_winner == DRAW:
            pass
        else:
            scores[round_winner] += 1
            
        print(ROUND_MSG[round_winner])
        
        print('Score: cpu {} vs. {} you\n'.format(scores[CPU], scores[USER]))
    
    who_won = scores.index(max(scores))
    if who_won == CPU:
        print('CPU won the game')
    else:
        print('USER won the game')

def choice_cpu():
    """This function creates and returns the CPU's choice."""
    cpu = int(random_number_from_interval(0,len(OPTIONS)))
    if DEBUG:
        print('Hint: CPU chose {}'.format(OPTIONS[cpu]))
    return cpu

def choice_user():
    """This function asks the user for his/her choice and returns it."""
    valid = False
    while not valid:
        option_string = '/'.join(OPTIONS)
        user_input = input('Choose an item out of {}: '.format(option_string)).lower()
        if user_input in OPTIONS:
            valid = True
        else:
            print('Incorrect input, please choose again.')
    return OPTIONS.index(user_input)
    

def compare(cpu, user):
    """
        This function compares the random CPU-choice with the user's input
        and returns who won (CPU, USER, DRAW)
    """
    # rows: cpu   cols: user
        #ROCK   PAPER  SCISCCOR
    matrix = [
        [DRAW,  USER,  CPU],  #ROCK
        [CPU,   DRAW, USER],  #PAPER
        [USER,  CPU,  DRAW]   #SCISCCOR
    ]
    return matrix[cpu][user]

main()