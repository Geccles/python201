with open("writing_files.txt", "w") as file:
    file.write("\nHello from python course 201")
    file.write("\n\tNew tabbed sentence")

with open("writing_files.txt", "r") as writingFile:
    content = writingFile.read()

print("The content of the file is:", content)
