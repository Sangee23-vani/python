# Write a function that computes the volume of a sphere given its radius

vol = lambda rad: (4/3) * (rad ** 3) * 3.14

print('Volume of sphere: {}'.format(vol(2)))


# Write a function that checks whether a number is in a given range (inclusive of high and low)

ran_check = lambda num,low,high : num in range(low,high+1)

print('\nIs number in given range: {}'.format(ran_check(5,2,7)))


# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

def up_low(s):
    print('\nOriginal string: {}'.format(s))

    up = list(filter(lambda letter: letter.isupper(),s ))
    print('No. of Upper case characters : {}'.format(len(up)))

    low = list(filter(lambda letter: letter.islower(), s))
    print('No. of Lower case characters : {}'.format(len(low)))

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)


# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(lst):       # by creating a dictionary we can remove duplications
    return list(dict.fromkeys(lst))

print('\nUnique list is {}'.format(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])))


# Write a Python function to multiply all the numbers in a list.

from functools import reduce

mul = lambda a,b : a*b

def multiply(numbers):
    return reduce(mul,numbers,1)

print('\nMultiplied list is {}'.format(multiply([1,2,3,-4])))


# Write a Python function that checks whether a passed in string is palindrome or not.

def palindrome(s):
    return s == s[::-1]

print('\nCheck palindrome {}'.format(palindrome('helleh')))


# HARD
# Write a Python function to check whether a string is pangram or not.

import string

def ispangram(str1):
    str2 = [ True if x in list(str1.lower()) else False for x in list(string.ascii_lowercase)]
    return False not in str2
list(string.ascii_lowercase)

print('\nIs pangram {}'.format(ispangram("The quick brown fox jumps over the lazy dog")))
