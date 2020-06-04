# args
def myfunc1(*rgs):
    print(rgs)             # looks like tuple
    print(rgs[4])
    return sum(rgs)
result = myfunc1(45,89,67,25,37,17)
print(result)


# kwargs
def myfunc2(**any):
    print(any)
    if 'k1' in any:
        return any['k1']
    else:
        return 'No Key'
result = myfunc2(k1='Hello',k2='Hai')
print(result)


# args and kwargs
def myfunc3(*x,**y):
    print(x)
    print(y)
    print('I would like to have {} {}'.format(x[2],y['food']))
myfunc3(10,20,40,23,food='Briyani',animal='dog')

def myfunc(s):
    for index,letter in enumerate(s):
        if index == 0:
            new_string = letter.upper()
        elif index%2 == 0:
            new_string = new_string + letter.upper()
        else:
            new_string = new_string + letter.lower()
    return new_string
data = myfunc('Sangeethavani')
print('Data {}'.format(data))