from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"

# Exercise: "Experiment with countries" (using functions, lists and for loops).

print('\n')

'''
For all 3 exercises shown below, I used the countries list from the 'countries.json' file.
'''


# Question 1 = Write a function that returns all the countries with the shortest country names / fewest characters.

def shortest_names (coutries: list) -> list:
    
    print('Elaboration question 1:\n')
    
    shortest_country_name = min(coutries, key=len)
    print(f'{shortest_country_name} = the country name with the fewest characters.\n')

    total_characters = len(shortest_country_name)
    print(f'{total_characters} = total characters of the country name with the fewest characters.\n')
    
    print('Below are all the countries with the shortest name / fewest characters from the \'countries\' list:\n')
    shortest_country_list = []

    for country in coutries:
        if len(country) == len(shortest_country_name):
            
            shortest_country_list.append(country)

    return shortest_country_list


# Question 2 = Write a function that returns a list that contains a top 3 of countries with the most vowels.

def most_vowels (countries: list) -> list:

    print('Elaboration question 2:\n')

    vowels = 'aeiou' + 'AEIOU'

    ranking_vowels = []
    ranking_top_three = []

    for country_name in countries:

        vowels_in_country = 0

        for vowel in country_name:
            if vowel in vowels:
                
                vowels_in_country += 1

        ranking_vowels.append([vowels_in_country, country_name])

    ranking_vowels.sort(reverse = True)

    print('Below is a list with the number of vowels in a country name including the country name. The list is sorted by the amount of vowels: from most vowels to fewest vowels.\n')
    
    print(ranking_vowels)
    print('\n')

    print('Below is a list of the top 3 countries with the most vowels:\n')
    
    for ranking in ranking_vowels[:3]:
        
        ranking_top_three.append(ranking[1])
        
    return ranking_top_three


# Question 3 = Write a function that returns a number of countries which can be used to form the alphabet.

def alphabet_set(countries: list) -> list:

    print('Elaboration question 3:\n')

    alphabet = list('abcdefghijklmnopqrstuvwxyz')
        
    print('Below is the alphabet in an iterable list:\n')
    
    print(alphabet)
    
    used_countries = []
    
    countries.sort(key = len, reverse = True)
    
    for country in countries:
        
        for letter in country.lower():
            if letter in alphabet:
                
                alphabet.remove(letter)
                
                if country not in used_countries:
                    
                    used_countries.append(country)

    print('\n')
    print('Below are the countries which I used to form the alphabet with:\n')
    
    return used_countries


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()
    
    """ Write the calls to your functions here. """

    print(shortest_names(countries))
    print('\n')
    print(most_vowels(countries))
    print('\n')
    print(alphabet_set(countries))
    print('\n')
