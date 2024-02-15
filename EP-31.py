# Day-31: Introduction to OOPS

"""
Class : It's a blue print
object : instance of class

A single class can have many objects
"""
a = 2
# a.
# print(type(a))

items = ["bat", "ball", "stumps"]
# items.

"""
In simple terms
datatype is class
and when we create a varible, it becomes object of that class
"""

class Person:
    #constructor
    def __init__(self):
        print("constructor called !")

    def display_info(self):
        print("In Display info funtion")

# Create an object of the Person class
person1 = Person()

# Access object attributes and methods
person1.display_info()
