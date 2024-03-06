# Day-52: Hierarchical Inheritance

"""
Hierarchical inheritance is a type of inheritance in which 
a single base class is inherited by multiple derived classes.
                    
            --------A--------
            |       |       |
            |       |       |
            B       C       D

"""

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

class Instructor(User):
    def create_course(self):
        print("create_course in Instructor class")
    def earnings(self):
        print("Earnings in Instructor class")

stud = Student()
stud.checkout()
stud.enroll()
stud.login()
stud.register()

inst = Instructor()
inst.create_course()
inst.earnings()
inst.login()
inst.register()