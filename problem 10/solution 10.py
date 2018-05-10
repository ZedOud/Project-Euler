#Project Euler #10
# Sum of primes before 2000000
def primes(x):
    yield(2)
    for i in range(3,x,2):
        if not any(not(i % y) for y in range(3,int(i**0.5)+1,2)):
            yield(i)
sum(primes(2000000))