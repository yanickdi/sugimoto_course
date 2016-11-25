"""
    BSP11 - Schere-Stein-Papier
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""

from lib import random_number_from_interval

#INPUT:
NUMBER_OF_GAMES = 5
OPTIONS = ['scissors', 'rock', 'paper']

choices = []
scores = [0, 0]

def main():
    pass

def choice_cpu():
    """This function creates and returns the CPU's choice."""
    choices.append('rock')
    #choices.append(OPTIONS[int(random_number_from_interval(0,len(OPTIONS)))])

def choice_user():
    """This function asks the user for his/her choice and returns it."""
    print(OPTIONS)
    choices.append(input('Choose an item from the list above: '))

def compare():
    """This function compares the random CPU-choice with the user's input."""
    if choices[0] == choices[1]:
        print('Draw!')
    elif choices[0] == OPTIONS[0] and choices[1] == OPTIONS[1]: # s->r
        scores[1] += 1
    elif choices[0] == OPTIONS[1] and choices[1] == OPTIONS[0]: # r->s
        scores[0] += 1
    elif choices[0] == OPTIONS[0] and choices[1] == OPTIONS[2]: # s->p
        scores[0] += 1
    elif choices[0] == OPTIONS[2] and choices[1] == OPTIONS[0]: # p->s
        scores[1] += 1
    elif choices[0] == OPTIONS[1] and choices[1] == OPTIONS[2]: # r->p
        scores[1] += 1
    elif choices[0] == OPTIONS[1] and choices[1] == OPTIONS[2]: # p->r
        scores[0] += 1
        

choice_cpu()
choice_user()
compare()
print(choices)
print(scores)

#main()