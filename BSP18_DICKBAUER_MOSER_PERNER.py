"""
    BSP 18 - Restgeld
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""

from lib import user_input, loaded_random_choice, random_number_from_interval

VISITORS = 30

ALTERNATIVE = True
ZZ_FIVE, ZZ_TEN = 1, 0
ALTERNATIVE_LIST = [ZZ_FIVE] * 15 + [ZZ_TEN] * 15
assert (ALTERNATIVE and VISITORS <= len(ALTERNATIVE_LIST)) or not ALTERNATIVE

P_10 = 0.6
P_5 = 1 - P_10


ZZ = [ZZ_TEN, ZZ_TEN, ZZ_TEN, ZZ_FIVE, ZZ_TEN] + [ZZ_FIVE] * 1000
i = -1
def loaded_random_choice(param):
    global i
    i += 1
    return ZZ[i]

def new_customer_has_a_5():
    """ Returns True if a new customer has a 5, False if 10"""
    if ALTERNATIVE: 
        choice_index = int(random_number_from_interval(0, len(ALTERNATIVE_LIST)))
        choice = ALTERNATIVE_LIST.pop(choice_index)
        return choice
    else:
        #random
        p_list = [P_10, P_5]
        return True if loaded_random_choice(p_list) == 1 else False


def main():    
    queue = []
    visits = 0
    fives = user_input([['How many notes to 5 Euro are in the cash desk', int, 1]])[0]
    tens = 0
    cum_queue_length = 0
    iterations = 0
    while visits < VISITORS or len(queue) > 0:
        if len(queue) > 0 and fives > 0:
            # serve the first visitor of the queue
            queue.pop(0)
            print('=> Visitor from the queue has been served.')
            fives -= 1
            tens += 1
        elif visits < VISITORS:
            is5 = new_customer_has_a_5()
            print('Note: {}'.format(5 if is5 else 10))
            print('Number of 5s in cash desk before: {}'.format(fives))
            print('Number of 10s in cash desk before: {}\n'.format(tens))
            visits += 1
            if is5:
                fives += 1
            elif not is5: #is10
                if fives > 0:
                    fives -= 1
                    tens += 1
                else:
                    queue.append(True)
                    print('<= Vistor goes into the queue.\n')
        else:
            print('{} visitors cannot be served.'.format(len(queue)))
            break
            
        iterations += 1
        cum_queue_length += len(queue)
        
    print('Average queue length: {:.2f}'.format(cum_queue_length / iterations))
    print('Average waiting time : {:.2f}'.format(cum_queue_length / visits))
    print('Utilization: {:.2f}'.format( (visits - len(queue)) / iterations))
            

main()

