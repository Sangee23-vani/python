# WARMUP SECTION:
print('WARMUP SECTION\n')

# LESSER OF TWO EVENS:
# Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)
print('LESSER OF TWO EVENS\t{}'.format(lesser_of_two_evens(4,56)))


# ANIMAL CRACKERS:
# Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(text):
    splited = text.lower().split()
    return splited[0][0] == splited[1][0]
print('ANIMAL CRACKERS\t{}'.format(animal_crackers('Eben Jenkin')))
print('ANIMAL CRACKERS\t{}'.format(animal_crackers('Jennis Joyal')))


# MAKES TWENTY:
# Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20.
# If not, return False
def makes_twenty(n1,n2):
    return n1 == 20 or n2 == 20 or n1+n2 == 20
print('MAKES TWENTY\t{}'.format(makes_twenty(20,34)))
print('MAKES TWENTY\t{}'.format(makes_twenty(12,8)))
print('MAKES TWENTY\t{}'.format(makes_twenty(23,78)))


# LEVEL 1 PROBLEMS
print('\nLEVEL 1 PROBLEMS\n')

# OLD MACDONALD:
# Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
    # first_letter = name[0].upper()
    # fourth_letter = name[3].upper()
    # return first_letter + name[1:3] + fourth_letter + name[4:]
    first_half = name[:3].capitalize()
    second_half = name[3:].capitalize()
    return first_half+second_half
print('OLD MACDONALD\t{}'.format(old_macdonald('sangi')))


# MASTER YODA:
# Given a sentence, return a sentence with the words reversed
def master_yoda(text):
    my_list = text.split()
    my_list = my_list[::-1]
    return ' '.join(my_list)
print('MASTER YODA\t{}'.format(master_yoda('I am pree')))


# ALMOST THERE:
# Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
    return abs(100-n) <= 10 or abs(200-n) <= 10         # abs() removes negative sign
print('ALMOST THERE\t{}'.format(almost_there(90)))


# LEVEL 2 PROBLEMS
print('\nLEVEL 2 PROBLEMS\n')

# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(my_list):
    for index,n in enumerate(my_list):
        if n == 3 and my_list[index+1] == 3:
            return True
        else:
            continue
    return False
print('FIND 33\t{}'.format(has_33([1,3,2,3,7])))


# PAPER DOLL:
# Given a string, return a string where for every character in the original there are three characters
def paper_doll(str):
    new_str = [letter+letter+letter for letter in str ]
    return ''.join(new_str)
print('PAPER DOLL\t{}'.format(paper_doll('sangi')))


# BLACKJACK:
# Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def blackjack(n1,n2,n3):
    total = n1+n2+n3
    my_tup = (n1,n2,n3)
    total_11 = my_tup.count(11)
    if total <= 21:
        return total
    elif total_11 > 0:
        total = total - (total_11 * 10)
        if total <= 21:
            return total
        else:
            return 'BUST'
    else:
        return 'BUST'
print('BLACKJACK\t{}'.format(blackjack(11,11,2)))
print('BLACKJACK\t{}'.format(blackjack(5,6,7)))      # --> 18
print('BLACKJACK\t{}'.format(blackjack(9,9,9)))        # --> 'BUST'
print('BLACKJACK\t{}'.format(blackjack(9,9,11)))       # --> 19


# SUMMER OF '69:
# Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6 and extending to the next 9
# (every 6 will be followed by at least one 9). Return 0 for no numbers.
def summer_69(my_list):
    if 6 not in my_list:
        return sum(my_list)
    else:
        index_6 = my_list.index(6)
        index_9 = my_list.index(9)
        return sum(my_list[0:index_6]) + sum(my_list[index_9+1:])
print('SUMMER OF 69\t{}'.format(summer_69([1,3,5,6,9,5])))


# CHALLENGING PROBLEMS
print('\nCHALLENGING PROBLEMS\n')

# SPY GAME:
# Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(my_list):
    if 0 in my_list:
        first_index = my_list.index(0)
        if 0 in my_list[first_index+1:]:
            second_index = my_list[first_index+1:].index(0) + first_index
            return 7 in my_list[second_index+1:]
        else:
            return False
    else:
        return False
print('SPY GAME\t{}'.format(spy_game([1,2,4,0,0,7,5])))           # --> True
print('SPY GAME\t{}'.format(spy_game([1,0,2,4,0,5,7])))           # --> True
print('SPY GAME\t{}'.format(spy_game([1,7,2,0,4,5,0])))           # --> False

def spy_game_sol(my_list):
    code = [0,0,7,'x']
    for num in my_list:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1
print('SPY GAME\t{}'.format(spy_game_sol([1,2,4,0,0,7,5])))           # --> True
print('SPY GAME\t{}'.format(spy_game_sol([1,0,2,4,0,5,7])))           # --> True
print('SPY GAME\t{}'.format(spy_game_sol([1,7,2,0,4,5,0])))           # -->


# COUNT PRIMES:
# Write a function that returns the number of prime numbers that exist up to and including a given number
def count_primes(n):
    primes = [2]
    x = 3
    if n < 2:
        return 0
    while x <= n:
        for y in range(3,x,2):
            if(x%y == 0):
                x += 2
                break
        else:                   # else for for loop. Unique behaviour in python
            x += 2
            primes.append(x)
    return len(primes)
print('COUNT PRIMES\t{}'.format(count_primes(100)))


# PRINT BIG:
# Write a function that takes in a single letter, and returns a 5x5 representation of that letter