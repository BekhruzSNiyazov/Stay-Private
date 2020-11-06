from sys import argv

filename = argv[1]
number = int(argv[2])

contents = ""

try:
    with open(filename, "r") as file:
        contents = file.read()
except: exit("Wrong file name was passed. Please, try again.")

try:    
    with open(filename, "w") as file:
        new_contents = ""
        for char in contents:
            new_contents += chr(ord(char)+number)
        file.write(new_contents)
except: exit("The pin code is too big. Try a smaller number.")