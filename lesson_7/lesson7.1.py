#Arrange string characters such that lowercase letters should come first
words = input("tur bar ")
y = ""
x = ""
for i in words:
    if i.islower():
        y = y + i
    else:
        x = x + i
print(y+x)


