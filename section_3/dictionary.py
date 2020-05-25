my_dictionary = {'k1':'v1', 'k2':'v2'}
my_dict = {'k1':23, 'k2':[4,7,9], 'k3':{'insideKey':5}}

print("my_dict['k2'] value {}".format(my_dict['k2']))
print("my_dict['k2'][1] value {}".format(my_dict['k2'][1]))

print("my_dict['k3'] value {}".format(my_dict['k3']))
print("my_dict['k3'][1] value {}".format(my_dict['k3']['insideKey']))

# To append new key value pair

my_dict['k4'] = 'New value'
print('\nAfter adding new Key value {}'.format(my_dict))

# Can overwrite value
my_dict['k1'] = 'I am overwritten'
print('After overwritten {}'.format(my_dict))

# Can list Keys
print('\nKeys {}'.format(my_dict.keys()))       # returns list

# Can list Values
print('Values {}'.format(my_dict.values()))

# Can view Items
print('Items {}'.format(my_dict.items()))       # returns list having tuples

# Is duplication of Keys allowed?

my_dict_with_duplication = {'k1':'v1','k2':'v2','k1':'v3'}
print('Duplication in Key {}'.format(my_dict_with_duplication))     # It overwrites the value