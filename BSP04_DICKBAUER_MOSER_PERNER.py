"""
    BSP 04 - Geburtstage
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""
DEBUG = False
OPTION = True # enables optional feature: print all birthdays and
               # mark those which occure more than twice
DAYS_IN_A_YEAR = 365

from lib import random_number_from_interval, user_input

def occurrences(input_list):
    """Searches a list and counts for each element in the list the number of its occurence
    The function returns a dictionary (hash table would be the corresponding type in matlab),
    where each element of the input_list is a key and the number of occurences the values
    e.g.
      [1,2,3] returns {1: 1, 2: 1, 3: 1}
      [1,1,2] returns {1: 2, 2: 1}
    """
    occ_dict = {}
    for elem in input_list:
        if elem in occ_dict:
            occ_dict[elem] += 1
        else:
            occ_dict[elem] = 1
    return occ_dict

def main():
    #user input:
    number_of_simulations, number_of_participants = user_input((
        ('Number of simulations', int, 2),
        ('Number of participants', int, 10)), DEBUG)
        
    simulation_results = []
    for simulation in range(number_of_simulations):
        # generate a list of birthdays - with length of participants
        birthday_list = []
        for i in range(number_of_participants):
            birthday_list.append( int(random_number_from_interval(0, DAYS_IN_A_YEAR))+1 )
        # count the same candidates:
        occ_dict = occurrences(birthday_list)
        assert sum(occ_dict.values()) == number_of_participants
        number_of_same_values = sum([value if value >= 2 else 0 for key, value in occ_dict.items()])
        simulation_results.append(number_of_same_values)
        
        # output only if option enabled:
        if OPTION:
            print('Ergebnisse aus Simulation {}/{}:'.format(simulation+1, number_of_simulations))
            print('{} von {} Personen haben am gleichen Tag Geburtstag (p={:.2f}%).\n'.format(
                number_of_same_values, number_of_participants, (number_of_same_values/number_of_participants)*100))    
            for birthday in birthday_list:
                # look if this one occures more than once
                if occ_dict[birthday] >= 2:
                    print(birthday, '*')
                else:
                    print(birthday)
                    
            for key, value in occ_dict.items():
                if value >= 2:
                    print('Am Tag {} haben {} Personen Geburtstag'.format(key, value))
            print()
    
    # result of all simulations
    overall_number_of_same_birthdays = sum(simulation_results)
    avg_number_of_same_birthdays = overall_number_of_same_birthdays / number_of_simulations
    simulation_result_p = avg_number_of_same_birthdays / number_of_participants
    
    print('Ergebnisse aller {0}/{0} Simulationen:'.format(number_of_simulations))
    print('Durchschnittlich haben {} von {} Personen am gleichen Tag Geburtstag.'.format(
        avg_number_of_same_birthdays, number_of_participants))
    print('WSKL ueber alle Simulationen: p={}%'.format(simulation_result_p * 100))
    
main()
