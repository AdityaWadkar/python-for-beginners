# Day-45: Introduction to Inheritance

"""
coding principle
DRY - DON'T REPEAT YOURSELF

Normal code

        Learning website

    student         Instructor
    -Register       -Register
    -login          -login
    -enroll         -Create Courses
    -checkout       -Check Earnings

DRY Code:- 

                User                                        Father
            - register                                  - black hair
            - login                             
                        
    Student         Instructor                      You              Brother/sister
    -Enroll         -Create Course              - black hair        -brown hair
    -Checkout       -Check Earnings             - dark skin color   - white skin color

Biggest benift of Inheritance
CODE RESUABILITY
Always goes in Bottom-UP approach


        Parent class       - Data member (variables in class)
            ^              - Member funtion/class methods
        Child class        - Class Constructors

    ** Private Members are not inherited of parent class in child class

"""

## Assignment - Take reacap of OOPs concept
#             - Explore about inheritance and post in comment section