inp = [int(i) for  i in input().split(' ')]
num1 =  max(inp)
num2 =  min(inp)
res1 = int(num1 / num2)
if  res1 * num2 == num1  :
    print('Multiples')
else :
    print("No Multiples")