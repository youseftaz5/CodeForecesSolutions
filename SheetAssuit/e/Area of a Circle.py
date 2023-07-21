import math 
from decimal import *
getcontext().prec = 11

inpFloat = Decimal(input()) 
area = pow(inpFloat,2) * Decimal(math.pi)
print(area)
