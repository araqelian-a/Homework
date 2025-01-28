#You are given three lists, list1, list2, and list3. Your task is to implement a
#programm that takes these lists and prints the following:
#The set of elements that are common to all three lists.
#The set of elements that are present in at least two of the three lists, but not in all
#three.
#The set of elements that are unique to each list (present in only one list).
Dates1 = [2007, 1999, 2004, 2005, 1936, 1777]
Dates2 = [2007, 2005, 1999, 2007, 1965, 1654]
Dates3 = [2007, 2004, 1984, 2005, 1965, 1684]
Dates1 = set(Dates1)
Dates2 = set(Dates2)
Dates3 = set(Dates3)
print(f"The set of elements that are common to all three lists{(Dates1 & Dates2) & Dates3}")
print(f"The set of elements that are present in at least two of the three lists, but not in allthree.{(Dates1 & Dates2 | Dates2 & Dates3) ^ (Dates1 & Dates3)}")
print(f"The set of elements that are unique to each list (present in only one list).{(Dates1 - Dates2 - Dates3) | (Dates2 - Dates1 -Dates3) | (Dates3 - Dates1 - Dates2 )}")









