# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'


# Exercise: "Organize movies and songs" (using functions and lists).

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

    print('Below is a sorted list of all the movies John Williams won a Golden Globe for, for composing the music for that movie:\n')

    movie_list.sort()

    return movies

print(alphabetical_order(movie_list))
print('\n')


# Question 2 = Write a function that takes a film name and returns 'True' or 'False' based on whether or not this movie won a Golden Globe by John Williams.

gg_movies = ['Jaws', 'Star Wars: Episode iv -- A New Hope', 'E.T. The Extra-Terrestrial', 'Memoirs of a Geisha']

'''
gg = golden globe
'''

def won_golden_globe(movies: str) -> bool:

    print('Elaboration question 2:\n')

    print('Below you can do a check if the composed music in a movie has won a Golden Globe by John Williams:\n')

    gg_movies_lower = [gg_movies.lower() for gg_movies in gg_movies]

    if movies.lower() in gg_movies_lower:
        print(movies, "=", True) # This is a double check to see if the function works.
        return True
    
    else:
        print(movies, "=", False)
        print('\n')
        return False
        
print(won_golden_globe('Jaws'))
print('\n')


# Question 3 = Write a function that returns a tidy list which only contains Golden Globe movie music composed by John Williams.

tidy_list = ['Jaws', 'Star Wars: Episode iv -- A New Hope', 'E.T. The Extra-Terrestrial', 'Memoirs of a Geisha', 'Fahrenheit', 'The Seventh One', 'Toto XX', 'Falling in Between', 'Toto XIV', 'Old Is New']

def remove_toto_albums(movies) -> list:
    
    print('Elaboration question 3:\n')

    print('Below you can see the tidied up list that only contains Golden Globe movie music composed by John Williams:\n')

    if "Fahrenheit" in tidy_list:
        tidy_list.remove("Fahrenheit")
    
    if "The Seventh One" in tidy_list:
        tidy_list.remove("The Seventh One")

    if "Toto XX" in tidy_list:
        tidy_list.remove("Toto XX")

    if "Falling in Between" in tidy_list:
        tidy_list.remove("Falling in Between")

    if "Toto XIV" in tidy_list:
        tidy_list.remove("Toto XIV")

    if "Old Is New" in tidy_list:
        tidy_list.remove("Old Is New")
    
    return movies

print('\n')
print(remove_toto_albums(tidy_list))
print('\n')