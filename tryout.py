def myfunc5(arg):
    args = list(arg)
    print('string to list', args)
    letterCount = 0
    for item in args:
        if letterCount % 2 == 0 and letterCount <= len(args):
            args[letterCount] = args[letterCount].upper()
        else:
            args[letterCount] = args[letterCount].lower()
        letterCount = letterCount+1

    print('sentence', args)

myfunc5('friENd nEed is A FrIend IN neED')