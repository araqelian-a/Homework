#Write a Python program to get the smallest number from a list.
x = [5, 2, 3, 1]
min = x[0]
for num in x:
    if num < min:
        min = num
print(min)


