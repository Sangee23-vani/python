my_tuple = ('a','b','c')

print('tuple my_tuple {}'.format(my_tuple))
print('tuple my_tuple[0:] {}'.format(my_tuple[0:]))

# Similar to list but this is Immutable

my_list = ['a','b','c']
my_list[1] = 'B'
print('\nMuted list {}'.format(my_list))

# my_tuple[1] = 'B'                             Throws error
# print('Muted Tuple {}'.format(my_tuple))

#Methods

count = my_tuple.count('a')
index = my_tuple.index('a')
print('Count {}'.format(count))     # May have any number of duplications of objects
print('Index {}'.format(index))     # Only return the first position of object
