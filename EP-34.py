# Day-34: Self 

"""
A function created inside class 
is called method
"""

class Person:
    #constructor
    def __init__(self):
        print("constructor called !")

    def display_info(self):
        print("In Display info funtion")

# Create an object of the Person class
person1 = Person()
person1.display_info()
person2 = Person()

"""
In python when we call a method,
The method gets default argument as method 
"""

# Access object attributes and methods

person2.display_info()


