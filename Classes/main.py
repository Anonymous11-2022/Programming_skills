# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Object Oriented Programming

print('\n')

'''
# Question 1 - part 1 = 'ValueError':

Write a class called 'Player' that is going to represent a soccer player. 

Define the Player class with the initialization method (__init__) so that it can receive the following arguments in this order:

- name (str)
- speed (float between 0 and 1)
- endurance (float between 0 and 1)
- accuracy (float between 0 and 1)
- If speed, endurance or accuracy is not between 0 and 1 (inclusive), a ValueError must be raised. Try using a for loop here to loop through those iterables and then define a valueError.

Save the given arguments as instance attributes with the following names:
- name
- speed
- endurance
- accuracy
'''

class Player():
    
    def __init__(self, name: str, speed: float, endurance: float, accuracy: float) -> str:

        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy

        for attribute in [speed, endurance, accuracy]:
            
            if attribute > 1 or attribute < 0:
                raise ValueError(F"- Please make sure that {attribute} is between 0 and 1.\n")


    '''
    # Question 1 - part 2 = 'Introduce':

    Define an instance method 'introduce' that takes no arguments (except self) and returns a string where 'Bob' is replaced by the player's actual name:
    
    - 'Hello everyone, my name is Bob.'
    '''

    def introduce(self):
        
        return F"- Hello everyone, my name is {self.name}.\n"


    '''
    Question 1 - part 3 = 'Strength':

    Now we want a method that returns us the best attribute of a player between the 3 we just defined (speed, endurance and accuracy). Define an instance method 'strength' that takes no arguments and returns a tuple with the name of its\
    attribute and its value. Imagine that the highest one is speed and the value is 0.8. Then the expected result should be like this: 

    ('speed', 0.8)

    If multiple attributes share the same value, prioritize as follows:

    - speed > endurance > accuracy
    '''

    def strength(self):
        
        best_results = (None, 0)
        
        for attribute in ["speed", "endurance", "accuracy"]:

            outcome_attribute = getattr(self, attribute)
            
            if outcome_attribute > best_results[1]:
                
                best_results = attribute, outcome_attribute

        return F"- Here is the name of the attribute with the highest value per player = {best_results}."


'''
# Question 2 - part 1 = 'Commentator':

Create a new class 'Commentator' and implement it in such a way that we can do this: 

- ray = Commentator('Ray Hudson')
- print(ray.name)
- Output = 'Ray Hudson'
'''


class Commentator():

    def __init__(self, name: str) -> str:

        self.name = name


    '''
    Question 2 - part 2 = 'Sum player':

    Write an instance method called 'sum_player' that takes an instance of a player and returns the sum of their 'speed', 'endurance' and 'accuracy'.

    To do this, define the method with two paramenters: 'self' and another one for the player. Then make it return a sum of a list of values retrieved with getattr() using the player as first parameter and the name of the attribute as\
    a string as the second parameter.
    '''

    def sum_player(self, player):

        attributes = ["speed", "endurance", "accuracy"]

        sum = 0

        for attribute in attributes:
            
            sum += getattr(player, attribute)

        return F"- The total sum of this player = {round(sum, 2)}."


    '''
    Question 2 - part 3-a = 'Compare_players':

    Write an instance method 'compare_players' that takes two instances of the class Player (in no particular order) and one of 'speed', 'endurance' and 'accuracy' as its arguments and returns the name of the player that scores the highest\
    on one of the 3 attributes.

    For example: 

    - alice = Player('Alice', 0.8, 0.2, 0.6)
    - bob = Player('Bob', 0.9, 0.2, 0.6)
    - print(ray.compare_players(alice, bob, 'speed'))
    - Output = 'Bob'

    If the players score equally on this attribute, return the name of the player that has the highest strength according to the strength function you just implemented.

    LET OP!!! De onderstaande instance 'compare_players' heeft meerdere vergelijkingen. Dus omdat Python altijd de code van boven naar beneden leest, zal er dus altijd gekeken worden naar de eerste vergelijking. Als de eerste vergelijking\
    niet het geval blijkt te zijn, dan zal Python kijken naar de 2e vergelijking enz. En al deze vergelijkingen hangen af van welke getallen je invult bij het aanroepen van de 'class Player helemaal onderaan deze code'.
    '''


    def compare_players(self, player_1, player_2, performance):

        performance_player_1 = getattr(player_1, performance)

        performance_player_2 = getattr(player_2, performance)
        
        if performance_player_1 > performance_player_2:

            return getattr(player_1, "name")

        elif performance_player_2 > performance_player_1:

            return getattr(player_2, "name")


        '''
        Question 2 - part 3-b = 'Highest strength according to the 'strength' instance':

        If the players score equally on 1 of the 3 attributes, return the name of the player that has the highest 'strength' according to the strength instance you just implemented.
        '''

        performance_player_1 = player_1.strength()[1]

        performance_player_2 = player_2.strength()[1]
        
        if performance_player_1 > performance_player_2:

            return getattr(player_1, "name")

        elif performance_player_2 > performance_player_1:

            return getattr(player_2, "name")


        '''
        Question 2 - part 3-c = 'Highest total score according to the 'sum_player' instance':

        If the 'highest strength' is also equal, report the name of the player that has the highest total score according to the 'sum_player' function / instance you just implemented.
        '''

        performance_player_1 = self.sum_player(player_1)
        
        performance_player_2 = self.sum_player(player_2)
        
        if performance_player_1 > performance_player_2:
            
            return getattr(player_1, "name")
            
        elif performance_player_2 > performance_player_1:
            
            return getattr(player_2, "name")
        
            '''
            Question 2 - part 3-d = 'Return string':

            If the 'sum_player' is also equal, return the string: 'These two players might as well be twins!'.
            '''
        
        else:
            return "These two players might as well be twins!"


if __name__ == "__main__":

# Attributes order = ["speed", "endurance", "accuracy"] 

# # Numbers for the answer to question 1 part 1 = This code returns a 'value error' if you enter an attribute value which is 1 or higher.\n").
    # rijkaard = Player("Frank Rijkaard", 1.8, 0.7, 0.6)
    # seedorf = Player("Clarence Seedorf", 0.9, 0.7, 0.6)

# Numbers for the answer to question 2 part 3-a = This code returns the name of the attribute with the highest value per player.
    rijkaard = Player("Frank Rijkaard", 0.8, 0.7, 0.6)
    seedorf = Player("Clarence Seedorf", 0.7, 0.8, 0.9)

# Numbers for the answer to question 2 part 3-b = If the players score equally on the same attribute, this code returns the name of the player that scores the highest 'strength' according to the 'strength' instance.
    # rijkaard = Player("Frank Rijkaard", 0.5, 0.4, 0.3)
    # seedorf = Player("Clarence Seedorf", 0.3, 0.4, 0.6)

# Numbers for the answer to question 2 part 3-c = If the players also score equally on the 'strength' instance, this code returns the name of the player that has the highest total score according to the 'sum_player' instance.
    # seedorf = Player("Clarence Seedorf", 0.1, 0.2, 0.3)
    # rijkaard = Player("Frank Rijkaard", 0.4, 0.5, 0.6)

# Numbers for the answer to question 2 part 3-d = If the players score is equal on all 3 attributes, this code returns the string: "These two players might as well be twins!
    # seedorf = Player("Clarence Seedorf", 0.1, 0.1, 0.1)
    # rijkaard = Player("Frank Rijkaard", 0.1, 0.1, 0.1)


    print("Elaboration question 1 - part 1 = 'ValueError':\n")
    print("- This 'value error' is only 'raised' if you enter an attribute value score of 1 or higher than 1.\n")

    print("Elaboration question 1 - part 2 = 'Introduce':\n")
    print(rijkaard.introduce())

    print("Elaboration question 1 - part 3 = 'Strength':\n")
    print(rijkaard.strength())
    print(seedorf.strength())

    print('\n')

    print("Elaboration question 2 - part 1 = 'Commentator':\n")
    winter = Commentator("Aron Winter")
    print(F"- The name of the 'Commentator' = {winter.name}")
    
    print('\n')

    print("Elaboration question 2 - part 2 = 'Sum Player':\n")
    print(winter.sum_player(seedorf))
    
    print('\n')

    print("Elaboration question 2 - part 3: a - d = 'Compare Players':\n")
    print(winter.compare_players(rijkaard, seedorf, "accuracy"))

    print('\n')
