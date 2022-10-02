import math
n = int(input())
x_list = list(map(int,input().split()))
y_list = list(map(int,input().split()))

p1D, p2D, p3D = 0, 0, 0
pinfD = []

for x, y in zip(x_list, y_list):
    p1D += abs(x-y)
    p2D += (x-y)**2
    p3D += abs(x-y)**3
    pinfD.append(abs(x-y))

print(p1D)
print(math.sqrt(p2D))
print(p3D**(1/3))
print(max(pinfD))
