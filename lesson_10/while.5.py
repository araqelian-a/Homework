#Write a Python program that calculates the Fibonacci sequence up to a given number n
#using a while loop. The Fibonacci sequence is a series of numbers where each number
#is the sum of the two preceding ones.
n = int(input("tur minchev qanisy "))
a = 0
b = 1
previous_a = 0
while a < n:
    print(a)
    previous_a = a
    a = b
    b = previous_a + b



