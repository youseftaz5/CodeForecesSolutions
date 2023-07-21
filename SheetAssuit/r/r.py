inp = int(input())
year = 365
month = 30
counterYear = 0
counterDay = 0
counterMon = 0
if inp < month:
    counterDay = inp
    print(f'{counterYear} years')
    print(f'{counterMon} months')
    print(f'{counterDay} days')
    

elif inp >= month and inp < year:
    x = inp // month
    z = inp % month
    print(f'{counterYear} years')
    print(f'{x} months')
    print(f'{z} days')


elif inp > year:
    qut = inp // year
    rem = inp % year 
    if rem >= month:
        qut1 = rem // month    
        m = rem % month
        print(f'{qut} years')
        print(f'{qut1} months')
        print(f'{m} days')

elif inp == year:
    a = inp // year
    print(f'{a} years')
    print(f'{counterMon} months')
    print(f'{counterDay} days')



