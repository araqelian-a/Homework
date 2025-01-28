#Input three integers. Output the word “Sorted” if the numbers are listed in
#a non-increasing or non-decreasing order and “Unsorted” otherwise.
a = int(input("tur arajin tivy "))
b = int(input("tur erkrord tivy "))
c = int(input("tur erord tivy "))
if a <= b <= c or a >= b >= c:
    print("sorted")
else:
    print("unsorted")




