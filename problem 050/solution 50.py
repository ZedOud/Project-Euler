#Project Euler #50
# Consecutive Prime Sums
p = []
for x in range(3,1000000,2):
    if x % 20000 == 1: print(x)
    sq = x**0.5
    for y in p:
        if x % y == 0:
            break
        if y > sq:
            p.append(x)
            break
    else: p.append(x)
print(len(p))
print(p[-10:])
m = []
for i in range(100, 600):
    if not i % 5: print(i)
    for x in range(len(p)-x):
        y = sum(p[x:x+i+1]) 
        if y in p:
            m.append(y)
        if y > 1000000:
            break
print(m[-10:])
print(m[-1])