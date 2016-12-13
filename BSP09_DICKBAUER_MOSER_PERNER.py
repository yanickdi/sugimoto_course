"""
    BSP 09 - Schiesssport
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""
from lib import random_number_from_interval, user_input

DEBUG = True
NUMBER_OF_SHOTS = 60

def main():
    # user input:
    number_of_series = user_input((
        ('Number of series', int, 200), ), DEBUG)[0]
    
    avg_score_list_normal = []
    avg_score_list_competition = [] 
    
    for i in range(number_of_series):
        score_list_serie_normal = []
        score_list_serie_competition = []
        for j in range(NUMBER_OF_SHOTS):
            x1,x2,y1,y2 = random_shot()
            score_normal = get_score(x1, y1)
            score_competition = get_score(x2, y2)
            score_list_serie_normal.append(score_normal)
            score_list_serie_competition.append(score_competition)
        average_score_normal = sum(score_list_serie_normal)/NUMBER_OF_SHOTS
        average_score_competition = sum(score_list_serie_competition)/NUMBER_OF_SHOTS
        avg_score_list_normal.append(average_score_normal)
        avg_score_list_competition.append(average_score_competition)
        
    # output
    print('The mean score per shot in normal is:',
          round(mean(avg_score_list_normal), 2))
    print('The variance of scores in normal is:', round(variance(avg_score_list_normal), 2))
    
    print('The mean score per shot in competition is:', round(mean(avg_score_list_competition), 2))
    print('The variance of scores in competition is:', round(variance(avg_score_list_competition), 2))
    
def random_shot():
    x_normal = int(random_number_from_interval(-4, 5+1))
    x_competition = int(random_number_from_interval(-3, 6+1))
    y_normal = int(random_number_from_interval(-2, 2+1))
    y_competition = int(random_number_from_interval(-2, 2+1))
    return x_normal, x_competition, y_normal, y_competition

def get_score(x, y):
    func_val = x**2 + y**2
    
    if func_val <= 1:
        return 10
    elif func_val <= 4:
        return 9
    elif func_val <= 9:
        return 8
    elif func_val <= 16:
        return 7
    elif func_val <= 25:
        return 6
    elif func_val <= 36:
        return 5
    elif func_val <= 49:
        return 4
    elif func_val <= 64:
        return 3
    elif func_val <= 81:
        return 2
    elif func_val <= 100:
        return 1
    else:
        return 0
        
def get_score_nerdy(x, y):
    func_val = x**2 + y**2
    boundaries = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
    for points in range(10, 0, -1):
        if func_val <= boundaries[len(boundaries) - points]:
            return points
    return 0

def mean(value_list):
    return sum(value_list)/len(value_list)

def variance(value_list):
    summands = []
    mean_value = mean(value_list)
    for value in value_list:
        summands.append((value - mean_value)**2)
    return mean(summands)

main()