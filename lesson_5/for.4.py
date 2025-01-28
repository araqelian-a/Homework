#Write a Python program to find the second smallest number in a list.
x = [25, 1, 1, 13]
min = second_small = int(input("tur mec tiv "))
for num in x:
    if num < min:
        min = num
    for num in x:
        if min < num < second_small:
            second_small = num
print(second_small)
