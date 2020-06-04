class Dog():
    def __init__(self,breed,name,age,spot):      # Like Constructor. self parameter mandatory
        self.breed = breed
        self.name = name
        self.age = age
        self.spot = spot

my_dog = Dog('Lab','Eben',3,False)               # Need not to give value for self
print('My Dog {} {} {} {}'.format(my_dog.name,my_dog.breed,my_dog.age,my_dog.spot))
print('Type of Object is {}'.format(type(my_dog)))