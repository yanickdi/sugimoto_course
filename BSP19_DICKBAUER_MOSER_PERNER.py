"""
    BSP 19 - Verdebliche Ware
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""

from lib import user_input, random_std

SIMULATION = 50
PROFIT = 3
OVERTIME_COST = .80 
SUNK_COSTS = 5


def main ():
    sum_profit_normal = 0
    sum_profit_overtime = 0

    for i in range(SIMULATION):
        # creation of random numbers according to normally distributed demand, production, ot distributions
        production = random_std(100000, 2000)
        demand = random_std(110000, 20000)
        overtime_production = random_std(10000, 200)
        # calculations for sales, costs, and profits
        sales_normal = min(production, demand)
        sales_overtime = min(production + overtime_production, demand)
        costs_normal = (production - sales_normal) * SUNK_COSTS
        costs_overtime = (production + overtime_production - sales_overtime) * SUNK_COSTS + overtime_production * OVERTIME_COST
        profit_normal = (sales_normal * PROFIT) - costs_normal
        profit_overtime = (sales_overtime * PROFIT) - costs_overtime
        sum_profit_normal += profit_normal
        sum_profit_overtime += profit_overtime
        
        print("Production:     {:>10.2f}, Demand:         {:>10.2f}, Overtime Production: {:>10.2f}".format(production, demand, overtime_production))
        print("Normal Costs:   {:>10.2f}, Normal Sales:   {:>10.2f}, Normal Profit:       {:>10.2f}".format(costs_normal, sales_normal, profit_normal))
        print("Overtime Costs: {:>10.2f}, Overtime Sales: {:>10.2f}, Overtime Profit:     {:>10.2f}".format(costs_overtime, sales_overtime, profit_overtime))
        print()
    
    print("Sum Profit Normal: {:>10.2f}, Sum Profit Overtime: {:>10.2f}".format(sum_profit_normal, sum_profit_overtime))
    
        
main()

