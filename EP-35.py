# Day-35: creating class

from fraction import Fraction
# a=2
num = Fraction(3,4)
print(num)
num2 = Fraction(34,43)
print(num2)


"""

Code of fraction.py file


class Fraction:
    def __init__(self, n, d):
        self.num = n
        self.den = d
    
    def __str__(self):
        return f"{self.num}/{self.den}"

"""