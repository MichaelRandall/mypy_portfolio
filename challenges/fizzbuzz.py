#!/usr/local/bin/python

# given a list of integers, prints fizz for any value that is a multiple of 3
# prints buzz for any value that is a multiple of 5, and for any value that
# is a multiple of 3 and 5 prints fizzbuzz

import sys, getopt

for numstr in sys.argv[1:]:
    num = int(numstr)
    if num % 3 == 0 and num % 5 == 0:
        print('fizzbuz')
    elif num % 3 == 0:
        print('fizz')
    elif num % 5 == 0:
        print('buzz')
    else:
        print(num)
