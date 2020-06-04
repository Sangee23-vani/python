my_list = [1,2,3,4,5]

# To know about any function structure
help(my_list.insert)

# basic function
def nameFunction(name = 'No name Given'):         # ''' is Optional, Can use with help(nameFunction)
    '''
    Docstring:  The function is to tryout some function behaviour
    input: no input
    return: nothing
    '''
    print('Hello {}'.format(name))
    return 'This is '+name

help(nameFunction)
nameFunction()              # Default argument will be taken
nameFunction('Sangi')

result = nameFunction('Pree')
print(result)

# def Check_dog(s):
#    if 'dog' in s.lower():
#       return True
#    else:
#        return False

def Check_dog(s):
    return 'dog' in s.lower()

result = Check_dog('Eben is my Dog')
print(result)

# pig word rules
# if word start with vowel add ay at the end
# else add first letter of the word at end with ay

def pig_latin(word):
    first_letter = word[0]
    if first_letter in 'aeiou':
        return word+'ay'
    else:
        return word[1:]+first_letter+'ay'

result = pig_latin('honey')
print('\n{}'.format(result))

result = pig_latin('apple')
print(result)