my_file = open('../test.txt')

# Methods

content1 = my_file.read()                # The cursor will move to the last position
my_file.seek(0)                          # To reset the cursor to 0th position(Command the line and check why its need)
content2 = my_file.read()

print('Read Content1\n{}'.format(content1))
print('\nRead Content2\n{}'.format(content2))   # After reading the file it doen't have anything

my_file.seek(5)
print('\nReadline\n{}'.format(my_file.readline()))

my_file.seek(0)
print('\nReadlines\n{}'.format(my_file.readlines()))    # returns list & Eachlines are considered separately

my_file.close()

# Also can name the file when opening

with open('../test.txt',) as my_f:
    content = my_f.read()
    print('\nContent from my_f\n{}'.format(content))

with open('../test.txt',mode='r') as f:
    print('\nMode r ->\n{}'.format(f.read()))
    f.seek(0)
    print('\nMode r again(run seek method before) ->\n{}'.format(f.read()))

with open('../test.txt',mode='a') as f:
    f.write('\nI am Fourth line')

with open('../test.txt',mode='r') as f:
    print('\nAfter appending\n{}'.format(f.read()))

with open('../test_write.txt', mode='w+') as f:
    f.write('I am the new file created via w mode')
    f.seek(0)
    print('\nRead in w+ mode\n{}'.format(f.read()))