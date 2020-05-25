# Numbers       -> Generally it's a numbers may have integers and floats to perform any of an arithmatic operation. In python we need not to specify the type
# Strings       -> Group cgaracters(also includes whitespaces, special characters, etc.,). Can be represented with single or double quotes
# Lists         -> Ordered items. Accessed through indexing and slicing. Mutable. Has several methods to easily perform any operation. Can overwrite the value with its index position. Represented with array brackets. Can have duplications and can have objects of any type
# Tuples        -> It's similar to lists but the only difference is immutable. Could not overwrite its value. Represented by paranthesis and only has two methods. That are count() and index(). Can have duplications and can have objects of any type
# Dictionaries  -> Unordered collection of records. Represented as key value pairs. Keys should be string. No duplication in keys. If any duplication occurs it will overwrite with the second value

# Numbers

# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25
equation = (4 / 2) ** 2 * 25 + 0.75 - 0.50

print('Equation is {}'.format(equation))
# What is the value of the expression 4 * (6 + 5)   -> 44
# What is the value of the expression 4 * 6 + 5     -> 29
# What is the value of the expression 4 + 6 * 5     -> 34
print('\n4 * (6 + 5) => {}\n4 * 6 + 5 => {}\n4 + 6 * 5 => {}'.format(4 * (6 + 5),4 * 6 + 5,4 + 6 * 5))

# What is the type of the result of the expression 3 + 1.5 + 4?     -> float
print('\ntype of 3 + 1.5 + 4 is {}'.format(type(3 + 1.5 + 4)))

# What would you use to find a number’s square root, as well as its square?
# To find square root =>    100 ** 0.5
# To find square      =>    10 ** 2



# Strings

s = 'hello'
# Given the string 'hello' give an index command that returns 'e'   -> s[1]
print('\nReturn e from hello by s[1] => {}'.format(s[1]))
# Reverse the string 'hello' using slicing
print('\nReversed string is {}'.format(s[::-1]))
# Given the string hello, give two methods of producing the letter 'o' using indexing
print('\nReturning o -> Method 1: s[4] => {}'.format(s[4]))
print('Returning o -> Method 2: s[-1] => {}'.format(s[-1]))


# Lists

# Build this list [0,0,0] two separate ways
list1 = [0,0,0]
# list 2
# Reassign 'hello' in this nested list to say 'goodbye' instead
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print('\nlist3 {}'.format(list3))
# Sort the list below
list4 = [5,3,4,6,1]
list4.sort()
print('Sorted list4 {}'.format(list4))


# Dictionaries

# Using keys and indexing, grab the 'hello' from the following dictionaries
d = {'simple_key':'hello'}
print('\nQ1 {}'.format(d['simple_key']))
d = {'k1':{'k2':'hello'}}
print('Q2 {}'.format(d['k1']['k2']))
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print('Q3 {}'.format(d['k1'][0]['nest_key'][1][0]))
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print('Q4 {}'.format(d['k1'][2]['k2'][1]['tough'][2][0]))


# Tuples

# What is the major difference between tuples and lists?    -> Tuple is immutable
# How do you create a tuple?
my_tuple = (1,2,3,4)


# Sets

# What is unique about a set?   -> It never allow duplication and only has the unique values
# Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print('\nAfter removing duplication with set {}'.format(set(list5)))


# Boolean

# For the following quiz questions, we will get a preview of comparison operators. In the table below, a=3 and b=4 without coding
a = 3
b = 4
# 2 > 3         -> False
# 3 <= 2        -> False
# 3 == 2.0      -> False
# 3.0 == 3      -> True
# 4**0.5 != 2   -> False

# What is the boolean output of the cell block below?
# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
# True or False?
# l_one[2][0] >= l_two[2]['k1']     -> false