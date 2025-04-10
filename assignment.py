with open("WEEK 4/laptop.txt", "w") as file:
    file.write("my laptop is HP corei5\n")
    file.write("its 8th generation\n")
    file.write("it has a 8GB RAM\n")

    print("File created successfully")

with open("WEEK 4/laptop.txt", "r") as file:
    content = file.read()
    print(content)

    modified_content = content.replace("HP", "generation 8").replace("DELL", "generation 6")
    
    with open("WEEK 4/laptop_modified.txt", "w") as new_file:
       new_file.write(modified_content)
    print("File modified successfully")
