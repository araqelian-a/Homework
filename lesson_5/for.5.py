#Write a Python program to remove duplicates from a list.
x = [5, 2, 3, 2]
y = []
for num in x:
    if num not in y:
        y.append(num)
print(y)

