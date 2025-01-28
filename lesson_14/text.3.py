# Write a Python script that takes multiple text files as input and concatenates their
# contents into a single text file
def concate_file(list_files):
    with open("new_text.txt", "a") as p:
        for i in list_files:
            with open(i, "r") as file:
                p.write(file.read() + "\n")
concate_file(["text.txt", "222.txt","555.txt"])
