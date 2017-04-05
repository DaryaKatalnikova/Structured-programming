import math

x=3
t=float(input("Write time"))
S=t**3-math.sqrt(t)
d=x*(t**(x-1))-1/2*math.sqrt(t)
print(S)
print(d)