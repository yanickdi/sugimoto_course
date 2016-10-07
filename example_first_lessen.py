import random

import lib
import matplotlib.pyplot as plt


def lifetime():
    cum_p = [0.05, 0.2, 0.4, 0.7, 0.9, 1]
    rand = random.random()
    for i, elem in enumerate(cum_p):
        if rand < elem:
            return i+1

def option_1():
    COSTS_REPAIR = 50
    COSTS_SERVICE = 25
    DURATION = 30
    MACHINES = 2

    costs = 0
    for m in range(MACHINES):
        t = 0
        while t < DURATION:
            t += lifetime()
            costs += COSTS_REPAIR
    return costs

def option_2():
    COSTS_REPAIR = 50
    COSTS_SERVICE = 25
    DURATION = 30
    MACHINES = 2
    t = 0
    costs = 0
    while t < DURATION:
        t1 = lifetime()
        t2 = lifetime()
        if t1 == t2:
            costs += 2 * COSTS_REPAIR
            t += t1
        else:
            costs += COSTS_REPAIR + COSTS_SERVICE
            t += min(t1, t2)
    return costs

def compare_and_show_plot():
    N = 500
    x = range(N)
    y1 = []
    y2 = []
    for i in range(N):
        cum_costs1 = 0
        cum_costs2 = 0
        for j in range(i+1):
            cum_costs1 += option_1()
            cum_costs2 += option_2()
        y1.append(cum_costs1/(i+1))
        y2.append(cum_costs2/(i+1))

    plt.plot(x, y1, label='Variante 1')
    plt.plot(x, y2, label='Variante 2')
    plt.legend()
    plt.xlabel('Anzahl an Simulationen')
    plt.ylabel('Kosten')
    plt.show()

if __name__ == '__main__':
    compare_and_show_plot()
    #option_2()