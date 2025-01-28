#Write a Python function to calculate the factorial of a number (a non-negative
#integer). The function accepts the number as an argument.
def factorial(a):
    i = 1
    result = 1
    while i <= a:
        result *= i
        i += 1
    return result
print(factorial(5))
