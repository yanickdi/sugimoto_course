"""
    BSP 21 - Lagerhaltung
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""

from lib import loaded_random_choice

NO_MACHINES = 3
CAP_STOCK_RAW_MATERIAL = 999999
CAP_STOCK_FINISHED_GOODS = 999999

PROCESSING_TIME = 1 # minute per machine 
FAULTY_PART_RATIO = 0.15 #???? TRITT DAS NUR 1X AUF ODER KÖNNTE DAS BEI JEDER MASCHINE PASSIEREN ALSO AUCH 3X PRO TEIL ???
GOOD_PART_RATIO = (1-FAULTY_PART_RATIO) 
EXTRA_TIME_FAULTY_PARTS = 4 # minutes

SIMULATION = 180 #minutes

#OUTPUT
# PRODUCTION, IDLE_TIME, UTILIZATION_OF_MACHINES, AVG_PROCESSING_TIME

def machine_processing():
    probability_list = [FAULTY_PART_RATIO, GOOD_PART_RATIO]
    x = loaded_random_choice(probability_list)
    if x == 1: 
        time = PROCESSING_TIME
    else
        time = PROCESSING_TIME + EXTRA_TIME_FAULTY_PARTS



def main ():
    machine_1_list = []
    machine_2_list = []
    machine_3_list = []
    stock_FG_list = []
    







main()