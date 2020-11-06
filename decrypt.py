from typing import ContextManager


filename = input("Please, enter the name of the file you want to decrypt: ")
number = int(input("Please, enter the pin code you should have remembered: "))

contents = ""

try:
    with open(filename, "r") as file:
        contents = file.read()
except: exit("Wrong file name was passed. Please, try again.")

try:    
    with open(filename, "w") as file:
        new_contents = ""
        for char in contents:
            new_contents += chr(ord(char)-number)
        file.write(new_contents)
except: exit("Wrond pin code was passed.")