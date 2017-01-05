"""
    BSP 21 - Lagerhaltung
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""
from lib import random_binom, random_poisson

SIMULATED_DAYS = 365

HOLDING_COSTS_PER_DAY = 2
SETUP_COSTS = 20
PENALTY_COSTS = 15

OPTION_BINOM = 0
OPTION_POISSON = 1

s = 2
q = 8
assert q >= s
assert 2 <= s <= 8
assert 2 <= q <= 8

def simulation(option):
    stock = 0
    sum_costs = 0
    for i in range(SIMULATED_DAYS):
        print('t={}'.format(i+1))
        print('Stock at the beginning: {}'.format(stock))
        if stock < s:
            #order q
            order_costs = SETUP_COSTS
            stock += q
        else:
            order_costs = 0
            
        if option == OPTION_BINOM:
            demand = random_binom(n=7, p=0.5)
        else:
            demand = random_poisson(lambd=3)
        
        sales = min(stock, demand)
        stock -= sales
        holding_costs = stock * HOLDING_COSTS_PER_DAY
        penalty_costs = (demand - sales) * PENALTY_COSTS
        period_costs = holding_costs + penalty_costs + order_costs
        sum_costs += period_costs
        
        # output of the actual period:
        print('Order: {}'.format(q if order_costs > 0 else 0))
        print('Demand: {}'.format(demand))
        print('Penalty Costs: {}'.format(penalty_costs))
        print('Period Costs: {}'.format(period_costs))
        print()
        
    return sum_costs
        
def main():
    print('Simulate Option a) - Binom:')
    sum_costs_binom = simulation(OPTION_BINOM)
    
    for i in range(5): print()
    
    print('Simulate Option b) - Poisson:')
    sum_costs_poisson = simulation(OPTION_POISSON)
    
    print('Sum costs of all periods of Option a: {}'.format(sum_costs_binom))
    print('Sum costs of all periods of Option b: {}'.format(sum_costs_poisson))
    
main()