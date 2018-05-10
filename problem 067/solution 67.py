#Project Euler #67
# Maximum path sum 2
# Find the maximum path of adjacent legs down the pyramid
# Done in #18

# Did a time profile
import time
t = time.time()

with open('p067_triangle.txt', 'r') as fi:
    p = fi.read()
rows = [[int(c) for c in row.split()] for row in p.splitlines()]

sums = [rows[0]]

for r in rows[1:]:
    s = [sums[-1][0]+r[0]]
    for i, c in enumerate(r[1:-1]):
        s.append(c + max(sums[-1][i:i+2]))
    s += [sums[-1][-1]+r[-1]]
    sums.append(s)

for r in rows[1:]: sums+=[[sums[-1][0]+r[0]]+[c+max(sums[-1][i:i+2])for i,c in enumerate(r[1:-1])]+[sums[-1][-1]+r[-1]]]

print(max(sums[-1]))

print('%.6fs'%(time.time()-t)) # 12353