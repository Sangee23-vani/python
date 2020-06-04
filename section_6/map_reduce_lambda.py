# map

my_list = [1,2,3,4,5]

def square(num):
    return num**2

new_list = list(map(square,my_list))
print('Map {}'.format(new_list))

# filter

def check_even(num):
    return num%2 == 0
# print(check_even(78))

filtered_list = list(filter(check_even,my_list))
print('Filter {}'.format(filtered_list))


# lambda function

# lambda num : num ** 2
square = lambda num : num ** 2
print(square(4))

print(list(map(lambda num : num * 5,my_list)))
print(list(filter(lambda num : num %2 == 0,my_list)))
