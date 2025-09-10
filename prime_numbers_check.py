import math

# Optimized Program to Check Prime Number

num = int(input("Enter a number: "))

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Only check up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
