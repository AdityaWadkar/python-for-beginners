# Day-55: Advanced File Operations & File Management


"""
example.txt file contents 

Hello world, Welcome to my youtube channel.
hello, my name is Aditya
my instagram account name is project_maker___

"""

# Opening a file in read mode
file = open("example.txt","r")

# Reading file content line by line
for line in file:
    print(line.strip())

# Closing the file
file.close()

# Opening a file in read mode
file = open("example.txt","r")

# Moving the cursor to the 5th byte from the beginning of the file
file.seek(10)
content = file.read()
print(content)

# Reading and printing the rest of the file content


# Closing the file
file.close()
