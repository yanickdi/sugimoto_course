"""
    BSP 25 - Zufallszahlenueberpruefung
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""

from lib import CongruenceGenerator, get_chi_squared, fact, user_input

DEBUG = False

def test_runtest(gen, runs):
    print('Runtest:')
    frequencies = {}
    pis = {}
    npis = {}
    for i in range(runs):
        last_val = -float('inf')
        count = 0
        while True:
            rand = gen.next_random()
            if rand > last_val:
                count += 1
            else:
                break
            last_val = rand
        # increase class `count` or initialise the class with value 1:
        frequencies[count] = frequencies.get(count, 0) + 1
     
    for class_nr in frequencies:
        pis[class_nr] = (1/fact(class_nr)) - (1/fact(class_nr + 1))
        npis[class_nr] = pis[class_nr] * runs
    
    t = sum([((frequencies[class_nr] - npis[class_nr])**2) / npis[class_nr] for class_nr in frequencies])
    df = len(frequencies)-1
    
    print('Frequencies: {}'.format(frequencies))
    # print test statistics t:
    chi_sq = get_chi_squared(df, 0.05)
    
    print('test statistic: {:.2f}, chi_sq: {:.2f}'.format(t, chi_sq))
    if t <= chi_sq:
        print('Random variables are signifcantly independent, grats!')
    else:
        print('Random are not signifcantly independent -> reject H1')

def test_indepency(randoms, lb, ub):
    print('Test on independency:')
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
        #print(class_nr)
        amount_in_class[class_nr] += 1
    # calc test statistics t \sum
    t = 0
    for i in range(r):
        t += (amount_in_class[i] - n*p_i)**2 / (n*p_i)
    # print test statistics t:
    chi_sq = get_chi_squared(r-1, 0.05)
    
    print('Amounts in class: {}'.format(amount_in_class))
    print('test statistic: {:.2f}, chi_sq: {:.2f}'.format(t, chi_sq))
    if t <= chi_sq:
        print('Random variables are signifcantly independent, grats!')
    else:
        print('Random are not signifcantly independent -> reject H1')

def generate_randoms(gen, amount):
    rand_list = []
    for i in range(amount):
        rand = gen.next_random()
        rand_list.append(rand)
    return rand_list
    
def main():
    cong_n, cong_b, cong_m = user_input([
        ('Parameter n of cong. generator', int, 2),
        ('Parameter b of cong. generator', int, 0),
        ('Parameter m of cong. generator', int, 110),], DEBUG)
    
    a = []
    for i in range(cong_n):
        ai, = user_input([
            ('Parameter a{} of cong. generator'.format(i+1), int, 13 + i*7)], DEBUG)
        a.append(ai)
    
    gen = CongruenceGenerator(n=cong_n, a=a, b=cong_b, m=cong_m)
    randoms = generate_randoms(gen, 100)
    test_indepency(randoms, 0, cong_m)
    print()
    test_runtest(gen, 36)
    
main()