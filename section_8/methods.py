# Functions inside the Class is called as Methods

class Dog():

    species = 'Mammal'

    def __init__(self,breed,name,age,spot):      # Like Constructor. self parameter mandatory
        self.breed = breed
        self.name = name
        self.age = age
        self.spot = spot

    def bark(self,number):
        print('{} barks as WOOF! and the number is {}'.format(self.name,number))

my_dog = Dog('Lab','Eben',3,False)               # Need not to give value for self

print('My Dog {} {} {} {}'.format(my_dog.name,my_dog.breed,my_dog.age,my_dog.spot))

my_dog.bark(23)



# EXAMPLE 2

class Circle():

    # CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self,radius = 1):
        self.radius = radius

    def get_circumference(self):
        return 2 * self.pi * self.radius

my_circle = Circle()
my_new_circle = Circle(7)
print(my_circle.get_circumference())
print(my_new_circle.get_circumference())

