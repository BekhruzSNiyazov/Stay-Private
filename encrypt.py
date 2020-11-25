import sys

try:
    filename = sys.argv[1]
    number = int(sys.argv[2])
except:
    sys.exit("Usage: encrypt filename number")

contents = ""

try:
    with open(filename, "r") as file:
        contents = file.read()
except:
    sys.exit("Wrong file name was passed. Please, try again.")

try:    
    new_contents = ""
    for char in contents:
        if char == "\n":
            new_contents += char
        else:
            new_contents += chr(ord(char)-number)
except:
    sys.exit("The pin code is too big. Try a smaller number.")

with open(filename, "w") as file:
    file.write(new_contents)