# Day-38: Encapsulation part2


"""
NOTHING IN PYTHON IS TRULY PRIVATE
"""
class ATM:
    def __init__(self):
        print("In constructor")
        #creating empty instances
        self.__pin=""
        self.__balance=0
        self.name=""

    def add_details(self,user_name,user_pin,user_balance):
        self.__pin = user_pin
        self.name = user_name
        self.__balance = user_balance
    
    def display_details(self):
        print(f"{self.name}'s PIN is {self.__pin}, and the balance is {self.__balance}.")

#creating multiple users
user1 = ATM()
user2 = ATM()

#assigning details
user1.add_details("abc","1234",4500)
user2.add_details("xyz","4321",2500)

#fetching details
user1.display_details()
user2.display_details()

# trap
# print("\nIn Trap 1")
# user1.balance=0
# user1.display_details()

"""
how private variables get store

__VariableName = _className__VaiableName
__pin = _ATM__pin

"""

# trap2
print("\nIn Trap 2")
user1.ATM__pin="546"
user1.display_details()

# but
user1._ATM__pin="345"
user1.display_details()

"""
REASON OF BEING NOT PRIVATE
"""