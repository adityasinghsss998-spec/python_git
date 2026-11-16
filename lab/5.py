# Random number prime check
import random


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


num = random.randint(1, 100)
print("Task 5: Random Number Prime Check")
print("Random number:", num)
if is_prime(num):
    print("The number is prime")
else:
    print("The number is not prime")
