# Day-32: Classes and Objects

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Create an object of the Person class
person1 = Person("John", 30)
person2 = Person("abc", 40)

# Access object attributes and methods
person1.display_info()
person2.display_info()
