x = [int(i) for i in input().split()]

sum  = x[0]  + x[1]
mult = x[0] * x[1]
mins = x[0] - x[1]

print(x[0], "+", x[1], "=", sum)
print(x[0], "*", x[1], "=", mult)
print(x[0], "-", x[1], "=", mins)