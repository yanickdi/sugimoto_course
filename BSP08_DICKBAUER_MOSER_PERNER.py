"""
    BSP 08 - Lotto
    Dickbauer Yanick 1030489, Patrick Moser 1114954, Perner Manuel 0633155
    WS 2016
"""
DEBUG = False
OPTION = True # enables optional feature: print all draws, bets
               # and number of right values
              

LOTTERY_MIN_VALUE = 1
LOTTERY_MAX_NUMBER = 45
LOTTO_FULL_MATCH = 6

from lib import random_choice, user_input

def main():
    # user input:
    number_of_bets = user_input((
        ('Number of bets', int, 8000),), DEBUG)[0]
    draw = lottery_numbers()
    print('Draw: {}\n'.format(pretty_bet_string(draw)))
    result = {i:0 for i in range(1, LOTTO_FULL_MATCH+1)}
    for i in range(number_of_bets):
        guessed_numbers = lottery_numbers()
        amount, match_list = check_lottery_ticket(draw, guessed_numbers)
        if amount > 0:
            result[amount] += 1
        if OPTION:
            print('Bet: {}, {} hits'.format(pretty_bet_string(guessed_numbers), amount))
    if OPTION:
        print()
    
    for key, value in result.items():
        theoretical_p = lotto_probability(key)
        simulated_p = value / number_of_bets
        print('{} hits:'.format(key))
        print('  {:.8f}% in simulation ({} times)'.format(simulated_p*100, value))
        print('  {:.8f}% theoretical probability\n'.format(theoretical_p*100))
    #print(result)

def pretty_bet_string(bet):
    return ', '.join('{:2d}'.format(numb) for numb in bet)

def lottery_numbers():
    """returns six random numbers between LOTTERY_MIN_VALUE and LOTTERY_MAX_NUMBER (a list)
    in ascending order"""
    numbers = []
    # create a `choices` list including all left choices (starting with 1..45)
    choices = list(range(LOTTERY_MIN_VALUE, LOTTERY_MAX_NUMBER+1))
    for i in range(6):
        # pick a random choice out of the choices list
        choice = random_choice(choices)
        choices.remove(choice)
        numbers.append(choice)
    return sorted(numbers)
    
def check_lottery_ticket(right_numbers, check_ticket):
    """this function compares how many numbers of `check_tickets` are also in the list `right_numbers`
    and returns two values: first, the amount of equal numbers and second: a list of equal_numbers"""
    equal_numbers = []
    for check_number in check_ticket:
        if check_number in right_numbers:
            equal_numbers.append(check_number)
    return len(equal_numbers), equal_numbers

def fact(number):
    prod = 1
    for i in range(1, number+1):
        prod *= i
    return prod

def bin_coeff(n, k):
    """returns binomialcoefficent of (n over k)"""
    return int(fact(n)/(fact(k)*fact(n-k)))

def lotto_probability(k):
    wanted_combinations = bin_coeff(LOTTO_FULL_MATCH, k)
    compl_wanted_comb = bin_coeff(LOTTERY_MAX_NUMBER - LOTTO_FULL_MATCH, LOTTO_FULL_MATCH-k)
    all_comb = bin_coeff(LOTTERY_MAX_NUMBER, LOTTO_FULL_MATCH)
    return (wanted_combinations * compl_wanted_comb) / all_comb



main()