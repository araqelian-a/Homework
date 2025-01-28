#Write a Python program that asks the user to enter a password. Keep asking for the
#password until the correct password "secret" is entered. Provide appropriate feedback
#to the user.
password = input("tur password ")
i = False
while i != True:
    new_password = input("tur entadrvox passwordy ")
    if new_password == password:
        i = True
        print(i)
    else:
        print("noric porci ")
