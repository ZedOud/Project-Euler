#Project Euler #4
import math

def pal(x):
    x = str(x)
    a = (x[:-len(x)//2])
    b = (x[math.ceil(len(x)/2.0):])
    return a == b[::-1]

skip = 900 # skips to checking 900-999
L = []
for x in range(1000)[skip:]:
    for y in range(1000)[skip:]:
        if pal(str(x*y)):
            L.append(x*y)
            
print(sorted(L)[-1])