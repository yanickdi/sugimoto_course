"""
    BSP 04 - Geburtstage
    Dickbauer Yanick 1030489, Patrick Moser 1114954, Perner Manuel 0633155
    WS 2016
"""
# INPUT:
NUMBER_OF_SIMULATIONS = 100
NUMBER_OF_PARTICIPANTS = 40
DAYS_IN_A_YEAR = 365

from lib import random_number_from_interval

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
    simulation_results = []
    for simulation in range(NUMBER_OF_SIMULATIONS):
        # generate a list of birthdays - with length of participants
        birthday_list = []
        for i in range(NUMBER_OF_PARTICIPANTS):
            birthday_list.append( int(random_number_from_interval(0, DAYS_IN_A_YEAR))+1 )
        # count the same candidates:
        occ_dict = occurrences(birthday_list)
        assert sum(occ_dict.values()) == NUMBER_OF_PARTICIPANTS
        number_of_same_values = sum([value if value >= 2 else 0 for key, value in occ_dict.items()])
        simulation_results.append(number_of_same_values)
        for key, value in occ_dict.items():
            if value >= 2:
                print('Am Tag {} haben {} Personen Geburtstag'.format(key, value))
        print()
            
        # output
        print('Ergebnisse aus Simulation {}/{}:'.format(simulation+1, NUMBER_OF_SIMULATIONS))
        for birthday in birthday_list:
            # look if this one occures more than once
            if occ_dict[birthday] >= 2:
                print(birthday, '*')
            else:
                print(birthday)
                
        print('{} von {} Personen haben am gleichen Tag Geburtstag (p={:.2f}%).\n'.format(
            number_of_same_values, NUMBER_OF_PARTICIPANTS, (number_of_same_values/NUMBER_OF_PARTICIPANTS)*100))
    
    # result of all simulations
    overall_number_of_same_birthdays = sum(simulation_results)
    avg_number_of_same_birthdays = overall_number_of_same_birthdays / NUMBER_OF_SIMULATIONS
    simulation_result_p = avg_number_of_same_birthdays / NUMBER_OF_PARTICIPANTS
    
    print()
    print('Ergebnisse aller {0}/{0} Simulationen:'.format(NUMBER_OF_SIMULATIONS))
    print('Durchschnittlich haben {} von {} Personen am gleichen Tag Geburtstag.'.format(
        avg_number_of_same_birthdays, NUMBER_OF_PARTICIPANTS))
    print('WSKL ueber alle Simulationen: p={}%'.format(simulation_result_p * 100))
    
main()
