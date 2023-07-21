inp = [i for i in input().split(' ')]
if '>' in inp:
    ans  = int(inp[0]) > int(inp[2])
    if ans is True:
        print('Right')
    else:
        print('Wrong')
if '<' in inp:
    ans  = int(inp[0]) < int(inp[2])
    if ans is True:
        print('Right')
    else:
        print('Wrong')
if '=' in inp:
    ans = int(inp[0]) == int(inp[2])
    if ans is True:
        print('Right')
    else:
        print("Wrong")