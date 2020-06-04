# __str__

class Book():

    def __init__(self,title,author):
        self.title = title
        self.author = author

    def __str__(self):              # Printing the object   -> print(Object)
        return 'The book {} written by {}'.format(self.title,self.author)

    def __len__(self):              # Finding the length of Object  -> len(object)
        return 23

    def __del__(self):
        print('The Book instance is deleted')

b = Book('Arasiyal Pazhagu','Samas')

print(b)                # Command __str__ function and run the program
print(str(b))

print(len(b))           # __len__

del b                   # __del__





