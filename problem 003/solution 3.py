#Project Euler #3
# Largest prime factor
def ch(x):
    for y in range(x)[2:]:
        if x % y == 0:
            return ch(x // y)
    return x
ch(600851475143)