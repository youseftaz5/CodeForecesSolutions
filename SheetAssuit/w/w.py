def apply(x , y , z, ret):
    if y == '+' and x + z == ret:
        print('Yes')
    elif y == '+' and x + z != ret:
        print(x + z)
    
    elif y == '-' and x - z == ret:
        print('Yes')
    elif y == '-' and x - z != ret :
        print(x - z)
    
    elif y == '*' and x * z == ret:
        print('Yes')
    elif y == '*' and x * z != ret:
        print(x * z)

inp      = [i for i in input().split(' ')]
right    = int(inp[4])
Fnumber  = int(inp[0])
operator = inp[1] 
Snumber  = int(inp[2])

apply(Fnumber,operator,Snumber,right)