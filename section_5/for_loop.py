# Lists
print('\nLists')
my_list = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for item in my_list:
    sum = sum + item
#    print('Sum is {}'.format(sum))
print('Sum is {}'.format(sum))


# Strings
print('\nStrings')
for letter in 'San':
    print(letter)

# Tuples
print('\nTuples')
my_tuple = (1,2,3,4)
for item in my_tuple:
    print(item)

# Tuple unpacking
print('\nTuple unpacking')
my_list = [('a','b','c'),('s','n','g'),('z','f','m')]
for item1,item2,item3 in my_list:
    print(item3)

# Dictionary
print('\nDictionary')
my_dict = {'k1':1,'k2':2,'k3':3}
print('Items {}'.format(my_dict.items()))
print('Keys {}'.format(my_dict.keys()))
print('Values {}'.format(my_dict.values()))

for item in my_dict:
    print('{}'.format(item))

for item in my_dict.items():
    print('{}'.format(item))

for key,value in my_dict.items():
    print('Key {} and the value is {}'.format(key,value))

for x in my_dict.keys():
    print(x)