# Day-46: Single Inheritance

class User:
    def register(self):
        print("register in user class")
    def login(self):
        print("login in user class")

class Student(User):
    def enroll(self):
        print("Enroll in student class")
    def checkout(self):
        print("checkout in student class")

#creating Student class object
# stud = Student()
# stud.checkout()
# stud.enroll()
# stud.login()
# stud.register()

# Creating User class object 
print("\n User class object \n")
u1 = User()
u1.login()
u1.register()



"""
Task :-
explore different types of inheritance
1. Single Inheritance
2. Multiple Inheritance
3. Multi-level Inheritance
4. Hybrid Inheritance

link :- https://www.geeksforgeeks.org/types-of-inheritance-python/

"""