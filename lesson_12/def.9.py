#Write a function that prints all prime numbers up to a given limit.
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True




def prime_numbers(n):
    for i in range(2, n+1):
        if is_prime(i):
            print(i)
prime_numbers(20)



