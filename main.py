filename = input("Please, enter the name of the file you want to encrypt: ")
number = int(input("Please, enter any pin code you'd like (you should remember it and it should not be too big): "))

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