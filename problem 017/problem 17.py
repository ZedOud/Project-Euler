#Project Euler #17
nums = ['','one','two','three','four','five',
        'six','seven','eight','nine','ten',
        'eleven','twelve','thirteen','fourteen','fifteen',
        'sixteen','seventeen','eighteen','nineteen']
tens = ['0-tens','1-tens','twenty','thirty','forty','fifty',
        'sixty','seventy','eighty','ninety']
powers = ['','thousand','million','billion','trillion']
def gName(a):
    c, n = 0, []
    def hun(a):
        return nums[a%20] if a//10%10 < 2 else tens[a//10%10]+('-'+nums[a%10] if a%10!=0 else '')
    while a > 0:
        if a%1000 != 0: 
            n.extend([powers[c], hun(a)])
            if a//100 > 0: n.append('and') 
            if a//100%10 != 0: n.append(nums[a//100%10] + ' hundred')
        a, c = a//1000, c+1
    m = [a for a in n[::-1] if a != '']
    return ' '.join(m)
print(sum(len(gName(y+1).replace('-','').replace(' ','')) for y in range(1000)))