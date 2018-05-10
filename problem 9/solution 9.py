#Project Euler #9
# Special Pythagorean triplet
# Find a pythag triplet that adds up to the limit
limit = 1000
bound = limit*0.005
for i in range(1, (limit//2)+1)[::-1]:
    a2 = i*i
    for j in range(1, ((limit-i)//3)+1):
        c = (a2 + j*j)**(1/2)
        if abs(round(c) - c) < 0.001:
            s = i + j + c
            if abs(s - limit) < bound:
                print(i, j, c, s, 'abc:', i*j*c)