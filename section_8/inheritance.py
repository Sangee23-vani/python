class Animal():
    def __init__(self):
        print('ANIMAL CREATED')

    def eat(self):
        print('I AM EATING')

    def who_am_i(self):
        print('I AM AN ANIMAL')

class Dog(Animal):

    species = 'Mammal'

    def __init__(self,breed):      # Like Constructor. self parameter mandatory
        Animal.__init__(self)
        print('DOG CREATED')
        self.breed = breed

    def bark(self,number):
        print('WOOF!')

    def who_am_i(self):
        print('I AM A DOG')

my_dog = Dog('Lab')               # Need not to give value for self

my_dog.eat()
my_dog.who_am_i()

