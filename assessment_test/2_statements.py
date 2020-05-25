# Use for, .split(), and if to create a Statement that will print out words that start with 's'

st = 'Print only the words that start with s in this sentence'
result = [x for x in st.split() if x[0] == 's']
print('Words start with s are {}'.format(result))

# Use range() to print all the even numbers from 0 to 10
my_list = [x for x in range(0,10) if x%2 == 0]
print('The result is {}'.format(my_list))

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3
my_list = [x for x in range(1,50) if x%3 == 0]
print('The result is {}'.format(my_list))

# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
my_list = ['even!' if (len(x)%2 == 0) else x for x in st.split()]
print('Result is {}'.format(my_list))

# Write a program that prints the integers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz"
my_list = ['Fizzbuzz' if (x%3 == 0 and x%5 == 0) else 'Fizz' if (x%3 == 0) else 'Buzz' if (x%5 == 0) else x for x in range(1,100) ]
print(('Result is {}'.format(my_list)))

# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
my_list = [x[0] for x in st.split()]
print('Result is {}'.format(my_list))