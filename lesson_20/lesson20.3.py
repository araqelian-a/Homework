# Given a list of numbers, write a function to find the sum of all numbers in the list that
# can be divided by 7.

def sum_numbers_divide_7(numbers):
    sum = 0
    for i in numbers:
        if i % 7 == 0:
            sum += i

    return sum
print(sum_numbers_divide_7([7, 14, 21, 3, 4, 5]))


