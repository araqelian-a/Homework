# Write a Python program to find if a given string starts with a given
# character using Lambda.
string = "$%$#$#$asdasd12"
result = lambda x: x == string[0]
character = input("give character ")
print((result(character)))