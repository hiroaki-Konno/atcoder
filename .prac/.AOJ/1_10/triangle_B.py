import math
a, b, C = map(int, input().split())

S = a * b * math.sin(math.radians(C)) / 2
c = math.sqrt(a**2 + b**2 -(2*a*b*math.cos(math.radians(C))))
L = a + b + c
h = S * 2 / a
print(S)
print(L)
print(h)