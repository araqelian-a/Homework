#Print a square pattern using a nested for loop. The pattern should have 5 rows and 5
#columns.

h = " "
for i in range(1, 3):
    for j in range(1, 4):
       h = "*" * j
    print(h)
