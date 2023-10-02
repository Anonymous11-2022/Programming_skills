# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'


# Functions


# Exercise: Lists a.k.a. "Let’s binge and roll" (using functions and lists).

'''
For this exercise I had to use the following websites to find the necessary movies and songs:

- https://en.wikipedia.org/wiki/List_of_awards_and_nominations_received_by_John_Williams
- https://en.wikipedia.org/wiki/Joseph_Williams_(musician).
'''

# Question 1 = Write a function that returns a list of strings (for movies in this case) in alphabetical order.

movie_list = ['Jaws', 'Star Wars: Episode iv -- A New Hope', 'E.T. The Extra-Terrestrial', 'Memoirs of a Geisha']

def alphabetical_order(movies: list) -> list:
    
    print('\n')
    print('Elaboration question 1:\n')

    print('Below is a sorted list of all the movies for which John Williams composed the music for and also won a Golden Globe for:\n')

    movie_list.sort()

    return movies

print(alphabetical_order(movie_list))
print('\n')


# Question 2 = Write a function that takes a film name and returns 'True' or 'False' based on whether or not this movie won a Golden Globe by John Williams.

gg_movies = ['Jaws', 'Star Wars: Episode iv -- A New Hope', 'E.T. The Extra-Terrestrial', 'Memoirs of a Geisha']

# gg = golden globe


def won_golden_globe(movies: str) -> bool:

    print('Elaboration question 2:\n')

    print('Below you can do a check if the composed music in a movie has won a Golden Globe by John Williams:\n')

    gg_movies_lower = [movie.lower() for movie in gg_movies]

    if movies.lower() in gg_movies_lower:
        print(movies, '=', True) # This is a double check to see if the function works.
        return True
    
    else:
        print(movies, '=', False)
        print('\n')
        return False
        
print(won_golden_globe('Jaws'))


# Question 3 = Write a function that returns a tidy list which only contains Golden Globe movie music composed by John Williams, without using a for loop.\
# But I created 2 tidy lists instead: 1 for John Williams and 1 for TOTO.😉

tidy_list_John = ['Jaws', 'Star Wars: Episode iv -- A New Hope', 'E.T. The Extra-Terrestrial', 'Memoirs of a Geisha', 'Fahrenheit',\
             'The Seventh One', 'Toto XX', 'Falling in Between', 'Toto XIV', 'Old Is New']

tidy_list_TOTO = []


def remove_toto_albums(tidy_list_John, tidy_list_TOTO) -> list:
    
    print('Elaboration question 3:\n')

    print('Even though the question was to write a function that returns 1 tidy list, I wrote a function that returns 2 tidy lists instead😉: 1 for John Williams and 1 for TOTO:\n')

    if 'Fahrenheit' in tidy_list_John:
        tidy_list_John.remove('Fahrenheit')
        tidy_list_TOTO.append('Fahrenheit')
    
    if 'The Seventh One' in tidy_list_John:
        tidy_list_John.remove('The Seventh One')
        tidy_list_TOTO.append('The Seventh One')

    if 'Toto XX' in tidy_list_John:
        tidy_list_John.remove('Toto XX')
        tidy_list_TOTO.append('Toto XX')

    if 'Falling in Between' in tidy_list_John:
        tidy_list_John.remove('Falling in Between')
        tidy_list_TOTO.append('Falling in Between')

    if 'Toto XIV' in tidy_list_John:
        tidy_list_John.remove('Toto XIV')
        tidy_list_TOTO.append('Toto XIV')

    if 'Old Is New' in tidy_list_John:
        tidy_list_John.remove('Old Is New')
        tidy_list_TOTO.append('Old Is New')
    
    return tidy_list_John, tidy_list_TOTO

print('\n')

tidy_lists = remove_toto_albums(tidy_list_John, tidy_list_TOTO)
tidy_list_John = tidy_lists[0]
tidy_list_TOTO = tidy_lists[1]

print('- Tidy list John Williams =', tidy_list_John, '\n')

print('- Tidy list TOTO =',tidy_list_TOTO, '\n')
