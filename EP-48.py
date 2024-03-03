# Day-48: Polymorphism


"""
POLYMORPHISM :- Geeks word (having multiple form)

Man - father,employee, husband, brother
women - mother, employee, wife, daughter

Types of Polymorphism

method overriding:- method overriding involves creating a method in the child class 
that has the same name, parameters, and return type as a method in the parent class.
class A:
    area(p1)
class B(A):
    area(p1)

Method overloading:- Method overloading refers to defining multiple methods with
the same name but different parameters within the same class
area(p1,p2)
area(p1)
are(p1,p2,p3)

Operator Overloading:- Operator Overloading is a feature that allows you to 
define custom behavior for built-in operators
"""


# class Phone():
#     def __init__(self,price,brand,version):
#         print("In Phone constructor")
#         self.price = price
#         self.brand = brand
#         self.version = version

#     def buy(self):
#         print("By method in Phone class")

# class SmartPhone(Phone):
    
#     def buy(self):
#         print("By method in smartphone class")

# apple = SmartPhone(150000,"Apple",15)
# print(apple.brand,apple.price,apple.version)

# apple.buy()


# some traps

class Parent:
    def __init__(self,age):
        print("In Phone constructor")
        self.age = age
    def get_age(self):
        return  self.age
class Child(Parent):
    def __init__(self,name,age):
        self.name = name
    
    def get_name(self):
        return self.name
    
ch = Child("Aditya",20)
print(ch.get_age())
