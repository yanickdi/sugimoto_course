"""
    BSP 14 - Manuelle Zufallszahlen
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
    
    Aufgabenstellung: Schreiben Sie ein Computerprogramm zur Erzeugung
                      von (0,1)-gleichverteilten Zufallszahlen für
                      a) Midsquare Methode
                      b) gemischte Kongruenzmethode
                      c) multiplikative Kongruenzmethode
                      
    Input:            Parameter je nach Methode
    Output:           Zufallszahlen
"""

# BSP A - MIDSQUARE
# INPUT:

def midsquare_method(seed):
    """Returns two values: an equal  distributed float between [0., 1.[ 
        calculated via the midsquare method and the second value is the
        next seed for next calculation
       seed: a number with the length of 4 (works also with a length
                                            less than 4)"""
    quadr = seed ** 2
    str_quadr = str(quadr)
    if len(str_quadr) < 8:
        str_quadr = ('0' * (8 - len(str_quadr))) + str_quadr
    
    next_seed = int(str_quadr[2:6]) #pos 2,3,4,5 are next seed
    
    # we want to return a random number from [0, 1[ - so we have to
    # normalize str_quadr
    #quadr is now a number between [0 and (9999**2)]
    std_rdn = quadr / (9999**2)
    return std_rdn, next_seed
    
def random_numbers_midsquare(n, start_seed):
    """retuns a list of n random numbers from 0 to excl 1"""
    rand_list = []
    seed = start_seed
    for i in range(n):
        rand, seed = midsquare_method(seed)
        rand_list.append(rand)
    return rand_list

def main():
    n = 100000
    rands = random_numbers_midsquare(n, 1234)
    print(sum(rands)/n)
    
main()

# BSP B - gemischte Kongruenzmethode
#INPUT

n = 4
a = 13
b = 2
m = 31
x_seed = 1

# Generate n random numbers
mixed_random_numbers = []

""" returns a list of n random numbers according to input parameters"""
for i in range (n):
    x_new = ((x_seed * a + b) % m)
    x_seed = x_new
    mixed_random_numbers.append(x_new)
    
print (mixed_random_numbers)

#BSP C - multiplikative Kongruenzmethode
multi_mixed_random_numbers = []

""" returns a list of n random numbers according to input parameters"""
for i in range (n):
    x_new = ((x_seed * a) % m)
    x_seed = x_new
    multi_mixed_random_numbers.append(x_new)
    
print (multi_mixed_random_numbers)

