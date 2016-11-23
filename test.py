from lib import random_number_from_interval


# INPUT:
NUMBER_OF_SERIES = 200

NUMBER_OF_SHOTS = 60

def main():    
    
    for i in range(1, NUMBER_OF_SERIES+1):
        score_list_normal = []
        score_list_competition = []  
        for j in range(1, NUMBER_OF_SHOTS+1):
            random_shot(x_normal, y)
            score_normal = 0
            #score_competition = 0
            
            score_normal += get_score(x_normal, y)
            #score_competition += get_score(x_competition, y)
        print(score_normal)
    #print(get_score(x_normal,y))
    #print(get_score(x_competition, y))
    #print(x_normal, x_competition, y)
    
def random_shot(x_normal, y):
    x_normal = int(random_number_from_interval(-4, 5+1))
    #x_competition = int(random_number_from_interval(-3, 6+1))
    y = int(random_number_from_interval(-2, 2+1))
    return x_normal, y

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
    

#print(get_score(x,y))
main()