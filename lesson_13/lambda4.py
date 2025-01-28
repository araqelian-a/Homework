#Write a Python program to find intersection of two given arrays using
#Lambda.
list1 = [1, 2, 3, 5, 7, 8, 9, 10]
list2 = [1, 2, 4, 8, 9]
print(list(filter(lambda x: x in list1, list2)))