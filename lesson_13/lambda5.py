#Write a Python program to add two given lists using map and
#lambda
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = lambda x, y: x + y
print(list(map(result, list1, list2)))