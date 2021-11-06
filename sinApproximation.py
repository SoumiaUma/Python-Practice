import math
x = math.pi
maxN2 = 5
sum = 0
for n in range(0,maxN2):
    term = ((-1)**n)*((x**(2*n+1))/(math.factorial(2*n+1)))
    sum += term
print('sin',x,'=',round(sum,4))