filename = input("What is the file name? ")
content = input("What is the content? ")

with open(filename, "w") as file:
    file.write(content)

openFile = input("Would you like to read this file? ")
if openFile in ["y", "n"]:
    if openFile == "y":
        with open(filename, "r") as file:
            print(file.read())
