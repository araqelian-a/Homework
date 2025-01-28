#Write a Python program to square and cube every number in a given list of
#integers using Lambda
numbers = [1, 2, 3, 4, 5]

print(f"squares = {list(map(lambda x:x ** 2, numbers))}")
print (f"cubes = {list(map(lambda x:x ** 3, numbers))}")