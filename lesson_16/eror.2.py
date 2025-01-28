#Write a function that removes an element at a specified index from a list. Handle the
#IndexError by raising a custom exception if the index is out of range.
def remove_element(l):
    try:
        l.pop(10)
        return l
    except IndexError:
        return "tenc index chka"
print(remove_element([1, 2, 3, 4]))
