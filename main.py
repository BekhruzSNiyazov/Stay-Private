filename = input("Please, enter the name of the file you want to encrypt: ")
number = int(input("Please, enter any number you'd like (you should remember it): "))

try:
    contents = ""

    with open(filename, "r") as file:
        contents = file.read()
    
    with open(filename, "w") as file:
        new_contents = ""
        for char in contents:
            new_contents += chr(ord(char)+number)
        file.write(new_contents)

except: exit("Error. Try again.")