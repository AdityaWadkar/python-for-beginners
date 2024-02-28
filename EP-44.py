# Day-44: Static variable/ class variable

"""
Task
IN ATM machine code we should assign
serial number to every customer/object


Static varibles comes in picture
when every object require a shared value

ex1- 
IFSC code of bank branch will same for all customers
pin,balance will be differnt for each customer(stored in instance varible)

ex2 - Degree name will same for every student in particular college
(CGPA will be differnt for each Student(stored in instance varible) )
"""

class ATM:
    srno = 1
    def __init__(self):
        print("In constructor")
        #creating empty instances
        self.pin=""
        self.balance=0
        self.name=""

        #decalring static varible
        self.srno = ATM.srno
        ATM.srno+=1

    def add_details(self,user_name,user_pin,user_balance):
        self.pin = user_pin
        self.name = user_name
        self.balance = user_balance
    
    def display_details(self):
        print(f"{self.srno}. {self.name}'s PIN is {self.pin}, and the balance is {self.balance}.")

#creating multiple users
user1 = ATM()
user2 = ATM()

#assigning details
user1.add_details("abc","1234",4500)
user2.add_details("xyz","4321",2500)

#fetching details
user1.display_details()
user2.display_details()

