#Project Euler #15
# Lattice paths, how many right and down paths on grid
# sum(2**x for x in xrange(21))*2 # nope
def pascal_side(n):
    r,o = [[1]],[0]
    for x in range(n*2+2): r+=[list(map(sum,zip(r[-1]+o,o+r[-1])))]
    return sorted(r[::2][n])[-1]
pascal_side(20)

#Project Euler #16
sum(int(x) for x in str(2**1000))