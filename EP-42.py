# Day-42: pass by reference

"""
If we can give integer, string, decimal etc
argument to funtion, then we can also give
object as argument to funtion
"""

##part1

# class Customer:
#     #method
#     def __init__(self,name):
#         self.name = name

# #function
# #passing object as argument in funtion greet
# def greet(cust_name):
#     print("Hello, ",cust_name.name)


# cust1 = Customer("Aditya")
# greet(cust1)



##part2
class Customer:
    #method
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

#function
def greet(cust_name):
    if cust_name.gender == "male":
        print("Hello, ",cust_name.name,"Sir !!")
    elif cust_name.gender == "female":
        print("Hi, ",cust_name.name, "Ma'am !!")

cust1 = Customer("Aditya","male")
cust2 = Customer("Yashasvee","female")
greet(cust1)
greet(cust2)

