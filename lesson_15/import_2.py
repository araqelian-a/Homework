#Write a function that generates a random password for the user. Allow the user to
# specify the length and complexity of the password (include letters, numbers, and
# symbols).
# Ogtvel random u string module-neric (string.ascii_letters,
# string.digits,string.punctuation, )
from string import ascii_letters
from string import punctuation
from string import digits

from random import choices

def generate_password(lengt,tiv,tar,symbol):
    password = ""
    digit = ""
    punction = ""
    string = ""
    qanak = 0
    if tiv:
        digit = digits
        password += str("".join(choices(digit)))
        qanak = 1
    if tar:
        string = ascii_letters
        password += str("".join(choices(ascii_letters)))
        qanak += 1
    if symbol:
        punction = punctuation
        password += str("".join(choices(punction)))
        qanak += 1

    h = digit + string + punction
    for i in range(0, lengt - qanak):
       x = ("".join(choices(h)))
       password = password + x
    return password
print(generate_password(3,True,True,True))



