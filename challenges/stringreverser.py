#!/usr/local/bin/python

# take input from a user and print it to the screen reversed

# prompt user for input and assign input to a variable
astring = input("Type a word or phrase enclosed in single or double quotes: ")

# reverse the input character by character and print to screen
print(astring[::-1])

# reverse only the words in the input and print to screen
newstr = astring.split()
newstr.reverse()
print(' '.join(newstr))


# use map function to reverse characters in a string
def strrev(str):
    return str[::-1]

myitem = map(strrev,newstr)

print(' '.join(myitem))