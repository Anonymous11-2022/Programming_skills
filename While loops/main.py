from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"


# While loops


'''
Question 1 = 'Implement a function called 'Unique Koala Facts':

This function takes an integer as an argument representing the number of unique koala facts you want to retrieve. It should return a list containing the requested number of unique facts.
There aren't too many unique facts in the dataset, so your function should be able to retrieve all of them. Set a limit of 1000 iterations to avoid infinite loops.

As always, start by defining the function with one argument.
Create two variables, one to count the number of loops (value 0) and another to set  max number of loops (value 1000). You can declare both with the same statement, just separating the names and the values with a comma.

- Create a variable with a blank list to store the facts.
- Start the loop: while the number of facts stored in the list is less than the number of requested facts...
- Create a new variable 'fact' using the random_koala_fact() function.
- If that fact is not already in the lists, add it.
- If the number of loops is greater than the max numer (1000), break the loop.

Make the function add +1 to the loop count variable. After doing so, make the function return the facts list.
'''

print('\n')

def unique_koala_facts (requested_facts: int) -> list:
        
    unique_facts = []
        
    count_begin, count_end = 0, 1000
    
    while len(unique_facts) < requested_facts:

        fact = random_koala_fact()
        
        if fact not in unique_facts:
            unique_facts.append(fact)

        if count_begin > count_end:
            break

        count_begin += 1
    
    return F"- Unique koala fact(s) = {unique_facts}"


'''
Question 2 = Implement a function called 'Number of Joey Facts':

Young marsupials are called 'joeys', and this function counts how many unique facts mention the term 'joey'. It does this by repeatedly getting facts from random_koala_fact until it has seen a particular fact 10 times.
Then, it returns the count of unique joey facts found in the dataset.

- Start defining the function. This time the argument can be blank: "()".
- Start declaring 3 variables: 1= to take a first fact from 'random_koala_fact()', 2= to count the times that first fact is seen, 3= to count the number of joey facts.
- Create another variable called 'unique_facts' with a blank list as a value.
- Start the while loop as followed: while the first seen fact is seen less than 10 times, create a new variable that gets another fact.
- Start using IF conditions.
- You need to add +1 to the variable that counts the amount of times the first fact is seen if both facts are the same.
- You need to add the fact to 'unique_facts' and if it is not already in the list, add it. Also, if "joey" is within that fact, add +1 to the counter and make sure that the facts are lower cased here.
- End by making the function return the number of joey facts.
'''

def num_joey_facts () -> int:

    fact = random_koala_fact()
    
    count_first_joey, count_total_joey = 0, 0

    unique_facts = []
    
    while count_first_joey < 10:
        
        another_joey_fact = random_koala_fact()
        
        if fact == another_joey_fact:
            count_first_joey += 1

        if another_joey_fact not in unique_facts:
            unique_facts.append(another_joey_fact)
            
            if 'joey' in another_joey_fact.lower():
                count_total_joey +=1
                print(F"- Sentence = {[another_joey_fact]}")
                print('\n')
    
    return F"- Total number of 'joey' facts = {count_total_joey}"


'''
Question 3 = Implement a function called 'Koala Weight':

We want to know the weight of a koala. This function retrieves the weight of a koala from the dataset. It searches for a fact containing the term 'kg' and extracts the numeric value. It then returns the weight as an integer in kilograms (kg).

- Start defining the function. This time the argument can be blank: "()"
- Create a fact variable that takes a fact from random_koala_fact()
- Use a while loop. This time you have to think about it a little different, as you want to keep looping through the iterables until it finds the 'kg' string, so use "not in".
- The moment the loops stops, make the function return an integer with the weight number.
'''

def koala_weight() -> int:

    weight_facts = random_koala_fact()

    while 'kg' not in weight_facts:
    
        weight_facts = random_koala_fact()
    
    print(F"- The sentence(s) which contains the weight of a koala = {weight_facts}\n")

    return F"- The koala weight = {int(weight_facts.split('kg')[0].split()[-1])}kg\n"
    

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.

if __name__ == "__main__":
    
    print("Elaboration question 1 = 'Unique Koala Facts':\n")
    
    # Below you can enter a number for how many 'koala facts' you would like te see.
    print(unique_koala_facts(2))

    print("\n")
    
    print("Elaboration question 2 = 'Number of Joey Facts':\n")
    print("Below are all the unique koala facts containing the word 'joey' in sentences and numbers:\n")
    print(num_joey_facts())
    
    print('\n')
    
    print("Elaboration question 3 = 'Koala Weight':\n")
    print(koala_weight())