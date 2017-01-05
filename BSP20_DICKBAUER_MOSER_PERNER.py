"""
    BSP 20 - Instandhaltung
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""

from lib import random_std

SIMULATION = 55000
NO_OF_VACUUM_TUBES = 4
COST_SHUTDOWN = 100
COST_TUBE = 20

def main ():
    
    vacuum_tube_list = []
    min_tube_lifetime = 0
    remain_hours = SIMULATION
    remain_hours_list = []
    
    while remain_hours >= 0:
        for i in range(NO_OF_VACUUM_TUBES):
            vacuum_tube_lifetime = random_std(1500, 500)
            vacuum_tube_list.append(vacuum_tube_lifetime)
            min_tube_lifetime = min(vacuum_tube_list)
  
            remain_hours = remain_hours - min_tube_lifetime
            remain_hours_list.append(remain_hours)
        print(remain_hours_list)
    
        
    
        





main ()