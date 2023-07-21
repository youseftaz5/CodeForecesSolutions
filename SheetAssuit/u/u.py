from decimal import Decimal
inp = Decimal(input())
case1 , case2 = int(inp) , inp-int(inp)
if case2 == 0.000:
    print(f'int {case1}')
else:
    print(f'float {case1} {case2}')
