import math
inp = [int(i) for i in input().split(' ')]
a,b,c,d = inp[0],inp[1], inp[2], inp[3]
r = b*math.log(a)-d*math.log(c)
if r > 0:
    print('YES')
else:
    print('NO')