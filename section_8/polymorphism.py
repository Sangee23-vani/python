# Example 1
class Dog():
    def __init__(self,name):
        self.name = name

    def says(self):
        print('{} says... WOOOF!'.format(self.name))

class Cat():
    def __init__(self,name):
        self.name = name

    def says(self):
        print('{} says... MEOW!'.format(self.name))

eben = Dog('Eben')
rosy = Cat('Rosy')

eben.says()
rosy.says()

# Example 2
class Animal():
    def __init__(self):
        print('Animal created')

    def says(self):
        raise NotImplementedError('Abstraction only created')

class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self)
        self.name = name

    def says(self):
        print('{} says... WOOOF!'.format(self.name))

class Cat(Animal):
    def __init__(self,name):
        Animal.__init__(self)
        self.name = name

    def says(self):
        print('{} says... MEOW!'.format(self.name))

# my_animal = Animal()
eben = Dog('Eben')
rosy = Cat('Rosy')

# my_animal.says()          -> Uncommand and run
eben.says()
rosy.says()

