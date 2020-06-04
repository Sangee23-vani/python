class Dog():

    # CLASS OBJECT ATTRIBUTES
    species = 'Mammal'                          # Common to all instances

    def __init__(self,breed,name,age,spot):      # Like Constructor. self parameter mandatory
        self.breed = breed
        self.name = name
        self.age = age
        self.spot = spot

my_dog = Dog('Lab','Eben',3,False)               # Need not to give value for self
print('My Dog {} {} {} {}'.format(my_dog.name,my_dog.breed,my_dog.age,my_dog.spot))

print('Class Object Attribute is {}'.format(my_dog.species))            # Refered with the instance