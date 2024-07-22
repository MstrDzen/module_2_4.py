numbers = [1, 50, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 131, 258]
primes = []
not_primes = []
is_prime = True

for i in numbers:
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                is_prime = False # Так и не разобрался, как её использовать в данном коде, без неё отлично всё работает.
                not_primes.append(i)
                break
        else:
            primes.append(i)
print(primes)
print(not_primes)