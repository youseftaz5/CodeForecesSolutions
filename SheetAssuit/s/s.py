from decimal import *

inp = Decimal(input())
if inp in range(0,26) or inp >= 0 and inp <= 25 :
    print(f'Interval [0,25]')    

elif inp in range(26,51) or  inp > 25 and inp <= 50:
    print(f'Interval (25,50]')

elif inp in range(51,76) or inp >= 50 and inp <=75:
    print(f'Interval (50,75]')

elif inp in range(76,101) or inp >= 75 and  inp <= 100:
    print(f'Interval (75,100]')

elif inp < 0 or inp > 100:
    print('Out of Intervals')