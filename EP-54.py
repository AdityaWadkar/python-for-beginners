# Day-54: Introduction to File Handling & Basic Operations

"""
different type of modes in file operation
w = writing mode
r = reading mode
x = execution mode
"""

# Opening a file in write mode
# file = open("example.txt","w")

# Writing content to the file
# file.write("hello viewers, welcome to my youtube channel.")

# Closing the file
# file.close()


# Opening a file in read mode
file = open("example.txt","r")

# Reading and printing the file content
content  = file.read()
print(content)

# Closing the file
file.close()
