# Write a function that takes two lists and returns a new list containing only the common
# elements. (without using set)
def conect_list(list1,list2):
    new_list = []
    for i in list1:
        if i in list2:
            new_list.append(i)
    return new_list

print(conect_list([1, 2, 4, 7, 8], [1, 4, 5, 6]))
