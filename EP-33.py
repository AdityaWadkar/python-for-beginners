# Day-33: Magic methods

"""
magic methods are predefined methods
Also called special methods or dunder methods
has "__methodName__"  (double underscore before and after method name )
"""
class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    #print()
    def __str__(self):
        return f"{self.title} by {self.author}"

    #len()
    def __len__(self):
        return self.pages

    # if name == "abs"
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    # if name < name2 
    def __lt__(self, other):
        return len(self) < len(other)

# Creating instances of Book class
book1 = Book("Harry Potter", "J.K. Rowling", 400)
book2 = Book("Lord of the Rings", "J.R.R. Tolkien", 500)

# Using special methods
# Calls __str__
print("Book 1:", book1)  

# Calls __len__
print("Length of Book 1:", len(book1)) 

# Calls __eq__
print("Are book1 and book2 equal?", book1 == book2)  

# Calls __lt__
print("Is book1 shorter than book2?", book1 < book2)  

#link to all magic methods :- 
# https://www.tutorialsteacher.com/python/magic-methods-in-python