# Day-36: Instance Variable

"""
Instance varible is a varible
for which the value of each object 
is different
"""

class ATM:
    def __init__(self):
        print("In constructor")
        #creating empty instances
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
user2 = ATM()

#assigning details
user1.add_details("abc","1234",4500)
user2.add_details("xyz","4321",2500)

#fetching details
user1.display_details()
user2.display_details()
