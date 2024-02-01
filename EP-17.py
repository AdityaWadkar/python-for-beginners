# DAY-17: Lists

"""
properties of list

Mutable :- Modify list elements
Ordered :- Access element based on index
Dynamic :- easy addition/removal of elements
Heterogeneous :- hold different data types
"""
# Lists
# list1 = [1,2,4]
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

# #type of list
# print(type(my_list))

# #length of list
# print(f"The length of list is {len(my_list)}")

# # type of data that we can store in list
# list1 = ["apple", "banana", "cherry"] #string data
# list2 = [1, 5, 7, 9, 3] # integer data
# list3 = [True, False, False] # boolean data
# list4 = ["apple",1,True] #mixed data
# print(list1)
# print(list2)
# print(list3)
# print(list4)

# # Accessing elements in a list
# print("Element at index 2:", my_list[2])

# # Slicing a list
# print("Sliced list:", my_list[1:4])

# # Modifying elements in a list
my_list[2] = 10
print("Modified list:", my_list)