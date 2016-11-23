"""
    BSP 08 - Lotto
    Dickbauer Yanick 1030489, Patrick Moser 1114954, Perner Manuel 0633155
    WS 2016
"""
# INPUT:
OPTION = True #Print every iteration
NUMBER_OF_BETS = 5

LOTTERY_MIN_VALUE = 1
LOTTERY_MAX_NUMBER = 45

from lib import random_choice

def main():
    draw = lottery_numbers()
    print('Draw: {}\n'.format(draw))
    result = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for i in range(NUMBER_OF_BETS):
        guessed_numbers = lottery_numbers()
        amount, match_list = check_lottery_ticket(draw, guessed_numbers)
        if amount > 0:
            result[amount] += 1
        if OPTION:
            beatiful_str = ', '.join('{:2d}'.format(numb) for numb in guessed_numbers)
            print('Tip: {}, {} hits'.format(beatiful_str, amount))
    if OPTION:
        print()
    
    for key, value in result.items():
        theoretical_p = lotto_probability(key)
        simulated_p = value / NUMBER_OF_BETS
        print('{} hits:'.format(key))
        print('  {:.8f}% in simulation ({} times)'.format(simulated_p*100, value))
        print('  {:.8f}% theoretical probability\n'.format(theoretical_p*100))
    #print(result)

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
    wanted_combinations = bin_coeff(6, k)
    compl_wanted_comb = bin_coeff(39, 6-k)
    all_comb = bin_coeff(45, 6)
    return (wanted_combinations * compl_wanted_comb) / all_comb



main()