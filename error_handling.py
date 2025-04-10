filename = input("Enter the name of the file: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print(content)
        
except FileNotFoundError:
    print("The file does not exist.please confirm the file name ")