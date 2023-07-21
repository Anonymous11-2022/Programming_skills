# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Exercise: strings a.k.a. "Soccer on a string"😉 (using operators, casting and strings).

'''
For this exercise I had to use the following website to find the necessary info:

- https://en.wikipedia.org/wiki/UEFA_Euro_1988_final

'''

# Part 1 - question 1 = Create a variable for every player that scored.

scorer1 = '- Ruud Gullit'
scorer2 = '- Marco van Basten'


# Part 1 - question 2 = Create a variable for each minute of the match that a goal was scored in.

goal_0 = 32
goal_1 = 54


# Part 1 - question 3 = Create a variable that stores a string that reports on who scored when \
# using the '+' operator to concatenate the variables and cast those whose datatypes are numbers into strings.

scorers = scorer1 + ' ' + str(goal_0) + ', ' + scorer2 + ' ' + str(goal_1)


# Part 1 - question 4 = Create a variable which will store a single string of information about who scored when during the match.

report = (F'{scorer1} scored in the {goal_0}nd minute\n{scorer2} scored in the {goal_1}th minute')


# Part 2 - question 1 = Choose a player's name and store it as a string.

player = 'Frank Rijkaard'


# Part 2 - question 2 = Use ‘slicing’ and ‘.find’ to isolate and store the player's first name.

first_name = player[0:player.find(" ")]


# Part 2 - question 3 = Find out the length of the surname of the player using len().

last_name_len = len(player[player.find(" "):] [:-1])


# Part 2 - question 4 = Isolate and store the player's initial and surname.

name_short = player[0:1] + '.' + ' ' +  player[player.find(" ")+1:]


# Part 2 - question 5 = Create a chant (for when the player has scored a goal)\
# containing the player’s first name and an exclamation mark (!) x-times,\
# where ‘x’ is equal to the number of characters in the player’s first name.\
# And make sure the last character of this string is not a space!

chant = (F'{first_name}! ' * len(first_name)) [:-1]


# Part 2 - question 6 = Create a boolean check to make sure that the last character of the chant is not a space.

good_chant = (chant[-1] != ' ')


print('\n')
# Part 1
print('Elaboration part 1 - question 1:\n')
print('Below are the players I selected from the UEFA Euro 1988 final:\n')
print(scorer1)
print(scorer2, '\n')

print('Elaboration part 1 - question 2:\n')
print('Below are the minutes of the match that a goal was scored in:\n')
print('-', goal_0)
print('-', goal_1, '\n')

print('Elaboration part 1 - question 3:\n')
print('Below is a string containing the name of the player followed by the minute the player scored during the match:\n')
print(scorers, '\n')

print('Elaboration part 1 - question 4:\n')
print('Below is a string containing a short report about who scored when in the match with use of the \'f-string\':\n')
print(report, '\n')

# #Part 2
print('Elaboration part 2 - question 1:\n')
print('Below is the player I chose for this question:\n')
print('-', player, '\n')

print('Elaboration part 2 - question 2:\n')
print('Below is the isolated first name of the player with the use of \'slicing\' and the \'.find\' function:\n')
print('-', first_name, '\n')

print('Elaboration part 2 - question 3:\n')
print('Below is the length of the player\'s surname with the use of len():\n')
print('- Player\'s surname =', last_name_len, 'long.' '\n')

print('Elaboration part 2 - question 4:\n')
print('Below are the isolated and stored initial and surname of the player:\n')
print('-', name_short, '\n')

print('Elaboration part 2 - question 5:\n')
print('Below is the number of chants equal to the number of characters in the player\'s first name and without the space behind the exclamation mark (!):\n')
print('-', chant, '\n')

print('Elaboration part 2 - question 6:\n')
print('Below is the boolean check to make sure that the last character of the chant isn\'t a space:\n')
print('- What is your answer to the following question: "Is the last character of the chant not a space? The answer =' ,good_chant, '\n')
