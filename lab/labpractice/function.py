def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n**2):
        if n % i == 0:
            return False
    return True


prime_count = 0
composite_count = 0
while True:
    n = int(input("enter the no (-1 to stop) : "))
    if n == -1:
        break
    if n <= 1:
        continue
    if is_prime(n):
        prime_count += 1
    else:
        composite_count += 1
print(prime_count)
print(composite_count)
