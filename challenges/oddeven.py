#!/usr/local/bin/python

"""
DOCSTRING: Prompts user to input a string and for every word in the string check if the number of characters is even or odd
"""

# prompt user for input and take user input and assign it to a list
userstr = input("Type a word, or a phrase seperated by spaces, and surrounded with quotes: ")

# loop through list of words determining word length and if even or odd number of characters
for word in userstr.split():
    if len(word) % 2 == 0:
        print("EVEN: " + word)
    else:
        print("ODD: " + word)