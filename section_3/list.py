my_list = ['Sangi', 'Pree', 'Eben', 45, 100.87, 'Thillai']

# To check the length -> len

print('Length\n')
count = len(my_list)
print('Length of my_list is {}'.format(count))

# Supports Indexing and Slicing

print('\nIndexing & Slicing\n')
print('my_list[0] is {}'.format(my_list[0]))
print('my_list[2:] is {}'.format(my_list[2:]))
print('my_list[2:5] is {}'.format(my_list[2:5]))
print('my_list[1:5:2] is {}'.format(my_list[1:5:2]))

# Concatenation

another_list = ['Kali', 'Jaggu', 'Kona']
new_list = my_list + another_list
print('\nConcatenated list is {}'.format(new_list))

# List values are mutable

new_list[2] = 'Abdul'
print('\nMuted list is {}'.format(new_list))

# List methonds

print('\nList Methods\n')

new_list.append('Keeri')
new_list.append('Magi')
print('Append {}'.format(new_list))

popped_item = new_list.pop(3)        # default position -> last
print('Pop {} and Popped item {}'.format(new_list,popped_item))

another_popped_item = new_list.pop(-7)
print('Pop {} and another Popped item {}'.format(new_list,another_popped_item))

char_list = ['z','s','a','d','e','x']
num_list = [3,6,9,2,3,7,6]
sorted_char_list = char_list.sort()     # Does not return anything
print('Sort Sorted_char_list is {}'.format(sorted_char_list))
print('Sort char_list after sorting is {}'.format(char_list))
num_list.sort()
print('Sort num_list after sorting is {}'.format(num_list))
char_list.sort()
num_list.sort()
print('Reverse char_list {}'.format(char_list))
print('Reverse num_list {}'.format(num_list))

tic_list = ['','','']
if 1 in tic_list or 2 in tic_list or 3 in tic_list or 4 in tic_list or 5 in tic_list or 6 in tic_list or 7 in tic_list or 8 in tic_list or 9 in tic_list:
    print('Good list')
else:
    print('bad list')
print(len(tic_list))

