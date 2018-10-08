#!/usr/local/bin/python

numbers = input("Enter a random number of integer values seperated by a space: ")
numlist = numbers.split()

output_string = ''
#num = 0

for numstr in numlist:
    num = int(numstr)
    if num % 3 == 0 and num % 5 == 0:
        output_string = output_string + 'fizzbuzz '
    elif num % 3 == 0:
        output_string = output_string + 'fizz '
    elif num % 5 == 0:
        output_string = output_string + 'buzz '
    else:
        output_string = output_string + '' + str(num) + ' '



print("Results: " + output_string)