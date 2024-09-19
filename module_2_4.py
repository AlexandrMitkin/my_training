numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
# primes.append(2)
for i in numbers:
    if i == 1:
        continue
    if i == 2:
        primes.append(i)
        continue
    if i % 2 == 0:
        not_primes.append(i)
        continue
    is_prime = True
    for j in range(3, i//2, 2):
        if i % j == 0:
            not_primes.append(i)
            is_prime = False
            break
    if is_prime == True:
        primes.append(i)
print(primes)
print(not_primes)
