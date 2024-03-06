# Day-51: Multilevel Inheritance

"""
Multilevel Inheritance in Python is a type of Inheritance that involves 
inheriting a class that has already inherited some other class

"""

# class Product():
#     def product_method(self):
#         print("In product method")
# class Phone(Product):
#     def phone_method(self):
#         print("In phone method")
# class Smartphone(Phone):
#     def smart_phone(self):
#         print("IN smart phone method")

# s1 = Smartphone()
# s1.smart_phone()
# s1.phone_method()
# s1.product_method()




class A():
    def a(self):
        print("a")
class B(A):
    def b(self):
        print("b")
class C(B):
    def c(self):
        print("c")
class D(C):
    def d(self):
        print("d")
class E(D):
    def e(self):
        print("e")
class F(E):
    def f(self):
        print("f")
class G(F):
    def g(self):
        print("g")
class H(G):
    def h(self):
        print("h")
class I(H):
    def i(self):
        print("i")
class J(I):
    def j(self):
        print("j")
class K(J):
    def k(self):
        print("k")

obj = K()
obj.a()
obj.b()
obj.c()
obj.d()
obj.e()
obj.f()
obj.g()
obj.h()
obj.i()
obj.k()

