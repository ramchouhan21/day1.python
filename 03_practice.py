# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that. 
import os

# specify the directory path
path = "."

# get list of files and directories
contents = os.listdir(path)

# print each item
for item in contents:
    print(item)