# Write a function that returns the nth largest element from a list.
def get_largest_element(list, n):
    h = len(list)
    for i in range(h):
        for j in range(h - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list[-n]

print(get_largest_element([1, 2, 5, 4, 8], 3))
