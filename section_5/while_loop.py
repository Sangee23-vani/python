x = 0

while x < 5:
    print(x)
    x += 1
else:
    print('x is greater than 5')

# break, pass and continue

print('\nContinue')
my_string = 'Thillai'
for letter in my_string:
    if letter == 'a':
        continue                # Go to the top of the closest enclosing loop
    print(letter)

print('\nBreak')
x = 0
while x < 5:
    if x == 3:
        break
    print(x)
    x += 1
else:
    print('x is greater than 5')

print('\nPass')
if True:
    pass
    # could not empty a control statement without pass
print('If statement passed')