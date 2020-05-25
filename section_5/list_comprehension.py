mylist = list(range(1,10))  # for my ref

mystr = 'Sangi'
# To convert this as list
list0 = [letter for letter in mystr]
print('String to list is {}'.format(list0))

list1 = [x for x in 'Hello world' if x=='o']
print('String to list is {}'.format(list1))

list2 = [x for x in range(0,20) if x%2 == 0]
print('String to list is {}'.format(list2))

list3 = [x**2 for x in range(0,20) if x%2 == 0 ]
print('String to list is {}'.format(list3))

# may consider as one line for loop

celcius = [45,32,45.7,65,12]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print('\nFahrenheit values are {}'.format(fahrenheit))

# if else

list4 = [x if x%2 == 0 else 'ODD' for x in range(0,10)]
print('\nMylist is {}'.format(list4))

# nested for loop

list5 = []
for x in [1,2,3]:
    for y in [1,10,100]:
        list5.append(x*y)
print('\nNested for traditional method: {}'.format(list5))

list6 = [x*y for x in [1,2,3] for y in [1,10,100]]
print('Nested for comprehension method: {}'.format(list6))

