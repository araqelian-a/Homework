#Write a function that generates a random password for the user. Allow the user to
# specify the length and complexity of the password (include letters, numbers, and
# symbols).
# Ogtvel random u string module-neric (string.ascii_letters,
# string.digits,string.punctuation,)
from string import ascii_letters
from string import punctuation
from string import digits

from random import choices

def generate_password(lengt,tiv,tar,symbol):
    password = ""
    if tiv == True and tar == True and symbol == True:
        for i in range(0, lengt):
            x = str("".join(choices(digits + ascii_letters + punctuation)))
            password = password + x
    if tiv == True and tar == False and symbol == False:
        for i in range(0, lengt):
            x = str("".join(choices(digits)))
            password = password + x
    if tiv == False and tar == False and symbol == True:
        for i in range(0, lengt):
            x = str("".join(choices(punctuation)))
            password = password + x
    if tiv == False and tar == True and symbol == False:
        for i in range(0, lengt):
            x = str("".join(choices(ascii_letters)))
            password = password + x
    if tiv == True and tar == True and symbol == False:
        for i in range(0, lengt):
            x = str("".join(choices(ascii_letters + digits)))
            password = password + x
    if tiv == True and tar == False and symbol == True:
        for i in range(0, lengt):
            x = str("".join(choices(punctuation + digits)))
            password = password + x
    if tiv == False and tar == True and symbol == True:
        for i in range(0, lengt):
            x = str("".join(choices(ascii_letters + digits)))
            password = password + x
    return password
print(generate_password(100, True , True , True))

