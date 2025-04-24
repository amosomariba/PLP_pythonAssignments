# Reading a file

file_path = "file.txt"

with open(file_path, "r") as file:
    content = file.read()
    print(content)

# Writing a file

file_path = "modify.txt"

with open(file_path, "w") as file:
    file.write("Hello there!! Amos")
