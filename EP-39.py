# Day-39: getters and setters

"""
Getters and Setters are standard/professional
way update private variables

"""

class ATM:
    def __init__(self):
        self.__pin=""
        self.__balance=0
        self.name=""

    def get_pin(self):
        print(f"{self.__pin}")
    def set_pin(self,new_pin):
        self.__pin = new_pin
        print("Pin Updated !")
        
        # if type(new_pin)==str:
        #     self.__pin = new_pin
        #     print("Pin Updated !")
        # else:
        #     print("Permission")

    def add_details(self,user_name,user_pin,user_balance):
        self.__pin = user_pin
        self.name = user_name
        self.__balance = user_balance
    
    def display_details(self):
        print(f"{self.name}'s PIN is {self.__pin}, and the balance is {self.__balance}.")

#creating multiple users
user1 = ATM()

#assigning details
user1.add_details("abc","1234",4500)

#fetching details
user1.display_details()

user1.get_pin()
user1.set_pin("4567")

user1.display_details()




