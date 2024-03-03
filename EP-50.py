# Day-50: Multiple Inheritance

"""
Multiple inheritance in Python is a feature that allows 
a class to inherit from multiple base classes. 
"""
###################### Multiple Inheritance ########################

"""
            parent1         parent2
               |               |
               |               |
               -----child-------
                

"""
class Parent1:
    def register(self):
        print("register in user class")
    def login(self):
        print("login in user class")

class Parent2():
    def enroll(self):
        print("Enroll in student class")
    def checkout(self):
        print("checkout in student class")

class child(Parent1,Parent2):
    def create_course(self):
        print("create_course in Instructor class")
    def earnings(self):
        print("Earnings in Instructor class")

# ch = child()
# ch.create_course()
# ch.enroll()
# ch.login()


"""
MRO :- Method resolution Order
"""

class Product1():
    def buy(self):
        print("In product1")
class Product2():
    def buy(self):
        print("In product2")
class client(Product2,Product1):
    pass

c = client()
c.buy()









