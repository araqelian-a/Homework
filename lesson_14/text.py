# Write a Python script that reads a text file (input.txt) and counts the
# occurrences of each character (including spaces and punctuation). Output the
# charactr frequency to another text file (output.txt).
with open("text.txt") as f:
    h = f.read()
    dict = {}
    for i in h:
        if i not in dict:
            dict[i] = 0
        dict[i] += 1
for k, v in dict.items():
    with open("qanak.txt", "a") as file:
        file.write(f"{k}: {v}\n")





