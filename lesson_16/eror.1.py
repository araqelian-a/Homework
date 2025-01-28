# Write a function that checks the length of a string provided by the user. Handle the
# TypeError by raising a custom exception if the input is not a string.
def toxi_erkarutyun(string):
    try:
        if not isinstance(string, str):
            raise TypeError
        print(len(string))
    except TypeError:
        print("string ches tve ")

toxi_erkarutyun([1, 2, 3, 4])

