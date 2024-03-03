# Day-49: Super keyword

"""
using super keyword we can call /invoke
parent class methods
It doesn't work outside class
"""
# code 1
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
#         super().buy() #super keyword declaration

# apple = SmartPhone(150000,"Apple",15)
# apple.buy()




#code 2
class Phone():
    def __init__(self,price,brand,version):
        print("In Phone constructor")
        self.price = price
        self.brand = brand
        self.version = version

class SmartPhone(Phone):
    
    def __init__(self,price,brand,version):
        self.price = price
        print("Inside smartphone constructor")
        super().__init__(price,brand,version)


apple = SmartPhone(150000,"Apple",15)

