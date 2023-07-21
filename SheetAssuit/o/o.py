inp = input()
deli = ['+','-','/','*']
for i in deli:
    if i in inp:
        (s) = i

ele = inp.split(s)
match s:
    case '+':
        print(int(ele[0]) + int(ele[1]))
    case '-':
        print(int(ele[0])- int(ele[1]))
    case '*':
        print(int(ele[0])* int(ele[1]))
    case '/':
        print(int(ele[0])/ int(ele[1]))
    case _:
        print('non') 