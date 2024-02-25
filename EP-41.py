# Day-41: Reference variable

"""
Reference variable is a variable
that point to memory address of object
"""

class ATM:
    def __init__(self):
        print("In constructor")
        #creating empty instances
        print(self)
        self.pin=""
        self.balance=0
        self.name=""

    def add_details(self,user_name,user_pin,user_balance):
        self.pin = user_pin
        self.name = user_name
        self.balance = user_balance
    
    def display_details(self):
        print(f"{self.name}'s PIN is {self.pin}, and the balance is {self.balance}.")

#creating multiple users
user1 = ATM()

#other of creating object
ATM()

"""
The is object is created in memory but it's lost
as  the address of object is not stored in any variable
Hence, in above example User1 is reference variable
"""

#assigning details
user1.add_details("abc","1234",4500)


#fetching details
user1.display_details()
