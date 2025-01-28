#Write a Python function to calculate count of each letter in string
def count_letters(string):
    letter_count = {}

    for i in string:
        if i in letter_count:
           letter_count[i] = letter_count[i] + 1
        else:
           letter_count[i] = 1
    return letter_count
print(count_letters("abrakadabra"))



