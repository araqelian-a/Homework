# Given a string, create a dictionary where keys are characters and values are their
# frequencies in the string.
string = "hello world "
len_string = {i: string.count(i) for i in string}
print(len_string)