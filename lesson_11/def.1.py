#Write a Python function to find the Max of three numbers.
def max_of_three(a, b, c):
    if a > b and a > c:
        max = a
    elif b > a and b > c:
        max = b
    elif c > a and c > b:
        max = c
    return max
print(max_of_three(1, 5, 4))
print(max_of_three(8, 4, 2))
print(max_of_three(5, 4, 8))