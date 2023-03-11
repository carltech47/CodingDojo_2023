"""
Challenge 1:
Create a loop that will print *every other* value in a list, starting with the value at index 0, index 2, etc.
For example (feel free to make up your own lists - use your own variables and values!):
my_list = [8, 1, "Hello", "green", True, 4, -1.5] # You should print 8, "Hello", True and -1.5 in this example
# Your loop goes here.
"""

mylist = ["apple", "banana", "pear", "blueberry", "strawberry", "orange", "raspberry", "lemon"]

for x in range(0, len(mylist), 2):
    print(mylist[x])


"""
Challenge 2:
Write a function that accepts a string as input and returns the number of vowels found in the string.
For this exercise, "a", "e", "i", "o" and "u" are vowels; we will not count "y" for this challenge.
If it helps, assume the string is all lower-case for now.  Then try to make it work regardless of if the
letters are upper- or lower-case.
For example: given "tommy", return 1 as "o" is a vowel, but "y" is not.  "adrian" should return 3.
"""
name = "Abrialla"

def ret_number_vowels(name):
    for i in range(0, len(name), 1):
        if i == "a":
            print("This name contains an", i)
        else:
            print(name[i])
    return i
            
ret_number_vowels("Abrialla")
ret_number_vowels("Torrey")

"""


"""


"""
Challenge 3:
Given a list of dictionaries as input in the format below, return a new list containing only the names.
Format:
some_variable = [
    {
        "name": "Adrian",
        "favorite_food": "Pizza",
        "favorite_number": 88
    },
    {
        "name": "Jenny",
        "favorite_food": "Sushi",
        "favorite_number": 24
    },
]
In this example, we should get ["Adrian", "Jenny"] as those are the names found.  Make this work for all lists,
so please make up your own examples!
"""
