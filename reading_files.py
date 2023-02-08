# opening a file and reading the content in there
with open("readme.txt", "r") as file:
    content = file.read()

print("The content of the file is:", content)
