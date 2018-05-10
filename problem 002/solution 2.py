#Project Euler #2
a,b,sum,num = 0,1,0,0
while sum < 4000000:
    num = a + b
    b, a = num, b
    if num % 2 == 0:
        sum += num
print(a,b,sum,num)


