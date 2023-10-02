# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

''' Question 1 = 'create Passport': 

Write a function called 'create_passport' that takes the following arguments:

- A name (str)
- A date of birth (str in ISO 8601 format, for example: 2002-12-31)
- A place of birth (str)
- A height in meters (float)
- A nationality (str)

Make sure that you stick to the order above. The function must return a passport dict containing this information with the keys:

- name
- date_of_birth
- place_of_birth
- height
- nationality 
'''

def create_passport(
        name, # = str
        date_of_birth, # = str in ISO 8601 format, for example: 2002-12-31
        place_of_birth, # = str
        height, # = in meters, float
        nationality # = str
        ) -> dict:

    return {
        'name' : name,
        'date of birth' : date_of_birth,
        'place of birth' : place_of_birth,
        'height' : height,
        'nationality' : nationality
    }

'''
Question 2 = 'Add Stamp':

Implement a function called 'add_stamp' which takes as its arguments, in this order, the following:

- A passport (dict) like the one returned by create_passport.
- A country (str).

Now the function should add (or update) a key-value pair to the dictionary:

- (key) 'stamps'
- (value) a list of countries (str) that the person has been to. For now you can create a blank list.

To do this, use a IF statement. If the new key is not in the passport, add it. Add a second IF statement that adds the country as the "stamps" value if the country is not in the list. Finish the function by making it return passport. 
'''

def add_stamp(passport, country) -> dict:

    if 'stamps' not in passport:
        passport['stamps'] = []     

    if country not in passport['stamps']:
        if passport['nationality'] != country:
            passport['stamps'].append(country)

    return passport


'''
Question 3 = 'Biometric Data'

Write a function called 'add_biometric_data' that takes as its arguments (in this order):

- A passport (dict), like the one returned by create_passport.
- A name (str) for the type of biometric data that will be added.
- The value, or values of the to-be-added biometric data ("value" is fine)
- A date in ISO format YYYY-MM-DD (str) for when the biometric data was recorded. 

The biometric data should live in a dictionary inside of the passport. In other words: a 'nested' dictionary is expected. The key for the biometric data dictionary is 'biometric'.

The function should return the following:

- If the passport did not yet have any biometric data: add the key for it. You can assume you'll only get passports with a chip to save biometric data.
- If the type of biometric data was not yet in the passport: add it to the passport.
- The value for the specific type of biometric data should again be a dictionary (so nested again). This dictionary should have two keys: date and value. See specific examples below.
- If the type of biometric data was already in the passport: update the biometric data in the passport, overwriting the previous value and date.

To do this, start writing the content of the function.

1. Create an If statement that checks if the "biometric" key is not there and then creates a nested blank passport.
2. Create a new dictionary called 'biometric_data' with two keys: "date" and "value", and give them the function arguments as value.
3. Target the "biometric" key within the passport and add the 'biometric_data' passport there.
4. Return the passport.
'''

def add_biometric_data(
        passport,
        biometric_type,
        biometric_value,
        biometric_date
        ) -> dict:

    if 'biometric' not in passport:
        passport['biometric'] = {}

    biometric_data ={'value' : biometric_value,
                    'date' : biometric_date
                    }
    
    passport['biometric'][biometric_type] = biometric_data
        
    return passport

print('\n')


if __name__ == '__main__':
    countries = get_countries()
    
    print("Elaboration question 1 = 'Create Passport':")
    passport = create_passport("James Bond", "1968-03-02", "London", "1,78", "British")
    print(passport)
    print("\n")

    print("Elaboration question 2 = 'Add Stamp':")
    stamp = add_stamp(passport, "The Netherlands")
    print(stamp)
    print("\n")

    print("Elaboration question 3 = 'Biometric Data':")
    james_bond = add_biometric_data(stamp, 'eyes_color', 'blue', '2023-07-31')
    print(james_bond)
    
    print('\n')
