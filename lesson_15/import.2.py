#Write a function that generates a random password for the user. Allow the user to
# specify the length and complexity of the password (include letters, numbers, and
# symbols).
# Ogtvel random u string module-neric (string.ascii_letters,
# string.digits,string.punctuation, )
from string import ascii_letters
from string import punctuation
from string import digits

from random import choices

def generate_password(lengt,complexity):
    password = ""
    if complexity == 0:
        for i in range(0, lengt):
            x = str("".join(choices(digits)))
            password = password + x
    if complexity == 1:
        for i in range(0, lengt):
            x = str("".join(choices(digits + ascii_letters)))
            password = password + x
    if complexity == 2:
        for i in range(0, lengt):
            x = str("".join(choices(digits + ascii_letters + punctuation)))
            password = password + x
    return password
# 0 = easy
# 1 = average
# 2 = hard
print(generate_password(2, 1))



