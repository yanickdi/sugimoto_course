"""
    BSP 08 - Lotto
    Dickbauer Yanick 1030489, Patrick Moser 1114954, Perner Manuel 0633155
    WS 2016
"""
# INPUT:
NUMBER_OF_BETS = 100000

LOTTERY_MIN_VALUE = 1
LOTTERY_MAX_NUMBER = 45

from lib import random_choice

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

def main():
    draw = lottery_numbers()
    result = {}
    for i in range(NUMBER_OF_BETS):
        guessed_numbers = lottery_numbers()
        amount, match_list = check_lottery_ticket(draw, guessed_numbers)
        if amount > 0:
            if amount in result:
                result[amount] += 1
            else:
                result[amount] = 1
    
    print(result)
"meine änderung"
main()