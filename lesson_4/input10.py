#Given the salaries of three employees working at a department, find the
#amount of money by which the salary of the highest-paid employee differs
#from the salary of the lowest-paid employee. The input consists of three
#positive integers - the salaries of the employees. Output a single number,
#the difference between the top and the bottom salaries
a = int(input("tur 1-iny "))
b = int(input("tur 2-y "))
c = int(input("tur 3-y "))
if a >= b and a >= c:
    maximum = a
elif b >= a and b >= c:
    maximum = b
elif c >= a and c >= b:
    maximum = c
if a <= b and a <= c:
    minimum = a
elif b <= a and b <= c:
    minimum = b
elif c <= a and c <= b:
    minimum = c
print(maximum - minimum)








