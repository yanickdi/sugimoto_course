"""
    BSP 25 - Zufallszahlenueberpruefung
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""

from lib import CongruenceGenerator
import random

def test_indepency(randoms, lb, ub):
    n = len(randoms)
    r = int(n ** (1/2))
    assert r <= 20
    range_of_class = (ub-lb) / r
    amount_in_class = [0 for i in range(r)]
    p_i = 1 / r # expected possibilty for a number in a class
    # assign my random numbers to one of the classes:
    for x in randoms:
        x = x - lb
        class_nr = int(x / range_of_class)
        amount_in_class[class_nr] += 1
    # calc test statistics t \sum
    t = 0
    for i in range(r):
        t += (amount_in_class[i] - n*p_i)**2 / (n*p_i)
    # print test statistics t:
    print(t)

def generate_randoms(amount, ub):
    gen = CongruenceGenerator(n=2, a=[13, 20], b=2, m=ub)
    rand_list = []
    for i in range(amount):
        rand = gen.next_random()
        rand_list.append(rand)
    return rand_list
    
def main():
    randoms = generate_randoms(100, 100)
    test_indepency(randoms, 0, 100)
    
main()