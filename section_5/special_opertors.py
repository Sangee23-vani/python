# range

for item in range(1,11):
    print(item)

my_list = list(range(1,4))
print(my_list)

# enumerate

for index,item in enumerate(my_list):
    print('Index: {} and Value: {}'.format(index,item))

for item in enumerate(my_list):
    print('Item: {}'.format(item))

# zip

my_list1 = [1,2,3,4,5,6]
my_list2 = ['a','b','c','d']
zipped_list = zip(my_list1,my_list2)
print(zipped_list)
final_list = list(zip(my_list1,my_list2))
print('Final zipped list is {}'.format(final_list))

for item in zip(my_list1,my_list2):
    print('Item {}'.format(item))

for list1item,list2item in zip(my_list1,my_list2):
    print('From list1 {} and list2 {}'.format(list1item,list2item))

# in

print('In function checkin {}'.format(3 in my_list1))                   # in list
print('In function checkin {}'.format('a' in 'Thillai Maharajan'))      # in string
print('In function checkin {}'.format('mykey' in {'mykey': 78658}))     # in dictionary
d = {'mykey': 78658}
print('In function checkin {}'.format(78658 in d))
print('In function checkin {}'.format(78658 in d.keys()))
print('In function checkin {}'.format(78658 in d.values()))

# min

print('Min function returns {}'.format(min(my_list)))
print('Max function returns {}'.format(max(my_list)))

# import

from random import shuffle
from random import randint

# shuffle

shuffle(my_list)
print('Shuffled list {}'.format(my_list))
shuffle(my_list)
print('Shuffled again {}'.format(my_list))

# randint

print('Randint between 0 to 100 is {}'.format(randint(0,100)))
print('Randint between 22 to 23 is {}'.format(randint(22,23)))

# input

result = input('Enter any Number here: ')
print('You have entered {} and the type is {}'.format(result,type(result)))
print('The int format of your data is {}'.format(int(result)))

age = int(input('Enter your age: '))
print('Your age is {}'.format(age))