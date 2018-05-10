#Project Euler #21
# Amicable Numbers >>> d[sum(ProperDivisors(x))] = x
def ProperDivisors(n):
    nums = [1]
    if n == 1 : return nums
    sq = int(n**0.5)
    for x in xrange(2,sq):
        if n % x == 0 : nums += [x, n//x]
    if n % sq == 0: nums.append(sq)
    return sorted(nums)

a = [0] + [sum(ProperDivisors(x)) for x in xrange(1,10000)]
sum(x for i,x in enumerate(a) if x < len(a) and a[x] == i and x != i)