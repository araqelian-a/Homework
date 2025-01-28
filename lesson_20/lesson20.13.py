# Write a function that checks if two sets are disjoint (have no common elements).
def check_set_joins(set1, set2):
    joins_element = set1 & set2
    return len(joins_element) != 0
print(check_set_joins({1, 2, 3, 4}, { 7 ,8, 9}))