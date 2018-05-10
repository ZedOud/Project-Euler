#Project Euler #12
# Highly divisible triangular number
# Find the first triangular number with > 500 factors
i = 0
while True:
    d, n = 2, sum(range(i))
    for x in range(2, int(n ** 0.5)):
        if not n % x:
            d += 2
    if d > 500: break
    i += 1
print(i, n)