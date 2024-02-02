# DAY-18: Tuples

"""
properties of Tuple

Immutable :- cannot Modify Tuple elements
Ordered :- Access element based on index
Fixed sized :- cannot perform addition/removal of elements
Heterogeneous :- hold different data types
"""

# Tuples
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# Accessing elements in a tuple
print("Element at index 3:", my_tuple[3])

# Slicing a tuple
print("Sliced tuple:", my_tuple[1:4])

#type of Tuple
print(type(my_tuple))

#length of Tuple
print(f"The length of Tuple is {len(my_tuple)}")

# type of data that we can store in Tuple
T1 = ("apple", "banana", "cherry") #string data
T2 = (1, 5, 7, 9, 3) # integer data
T3 = (True, False, False) # boolean data
T4 = ("apple",1,True) #mixed data
print(T1)
print(T2)
print(T3)
print(T4)


# Modifying elements in a Tuple
my_tuple[2] = 10 #generate and error
