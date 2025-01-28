# Implement a Python program that reads a text file (input.txt), prompts the user
# for a word to find, and another word to replace it with. Replace all occurrences of
# the first word with the second word and save the modified text to a new file
# (output.txt)
first_word = input("tur popoxvox bary = ")
second_word = input("tur nor bary = ")
with open("text.txt", "r") as file:
    h = file.read()
    h = h.replace(first_word, second_word)
with open("new_text.txt", "w") as file2:
    x = file2.write(h)