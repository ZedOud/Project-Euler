#Project Euler #44
# Pentagonal numbers
import time
def pen(x): return [n*(3*n-1)//2 for n in range(x)[1:]]
def fPair(y):
    ySet = set(y)
    sTime = time.time()
    for i in range(len(y)-1):
        for j in range(i):
            a, b = y[i], y[j]
            if a + b in ySet and abs(a - b) in ySet:
                    print (i,j, 'a=',a, 'b=',b, 'diff=',a-b, 'Run time:',time.time()-sTime)
fPair(pen(2500))