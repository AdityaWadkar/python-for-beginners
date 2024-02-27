# Day-43: Collection of objects

"""
we can store object as collection in 
list,dictionaries and tuples
"""
class Customer:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def disp(self):
        print(f"{self.name}'s age is {self.age} and gender is {self.gender}")

c1 = Customer("Aditya",23,"male")
c2 = Customer("Yashasvee",21,"female")
c3 = Customer("Pratik",22,"male")


L1 = (c1,c2,c3)

for i in L1:
    i.disp()

