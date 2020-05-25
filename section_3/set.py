my_set = set()
my_set.add(2)

# my_set.add([1,2,3])           Could not add list to set
my_set.add((1,2,3,3))             # Can add tuple in set
# my_set.add({'k1':'v1'})       Could not add dict to set

print('Set {}'.format(my_set))

# my_list = [1,1,1,1,2,2,2,3,3,3,3,[1,2,3,4]]       TypeError: unhashable type: 'list'
my_list = [1,1,1,1,2,2,2,3,3,3,3]
print('set(my_list) is {} where my_list is {}'.format(set(my_list),my_list))

my_tuple = (1,1,1,1,2,2,2,3,3,3,3)
print('set(my_tuple) is {} where my_tuple is {}'.format(set(my_tuple),my_tuple))

my_dict = {'k1':'v1','k2':'v2','k1':'v3'}
print('set(my_dict) is {} where my_dict is {}'.format(set(my_dict),my_dict))    # Only takes Key
