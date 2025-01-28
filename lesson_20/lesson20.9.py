# Write a function that finds the key with the maximum value in a dictionary.
def get_maximum_value(dict):
    max_value = 0
    for k, v in dict.items():
        if v > max_value:
            max_value = v
    return max_value
print(get_maximum_value({"a":10, "b":20, "c":5}))