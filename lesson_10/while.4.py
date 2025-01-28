#Write a Python program that generates a random number between 1 and 100 and asks
#the user to guess the number. The program should give hints whether the guessed
#number is too high or too low until the correct number is guessed.
num = int(input("tur gaxtni tivy 1-100 "))
i = False
while i != True:
    new_num = int(input("tur entadrvox patasxany "))
    if new_num == num:
        i = True
        print(i)
    elif new_num < num:
        print("cacr tiva porci noric ")
    elif new_num > num:
        print("barcr tiva porci noric ")

