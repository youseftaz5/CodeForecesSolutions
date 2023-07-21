inp = [int(i) for i in input().split(' ')]
result = inp[0] * inp[1] * inp[2] * inp[3]
final = list(str(result))
final.reverse()
final1 = final[1]
final0 = final[0]
# strResult = str(final[1]) str(final[0]) 
print(f'{final1}{final0}')