n, m, l = map(int, input().split())

A = []
B = []
""" 
1 2
0 3
4 5

1 2 1
0 3 2 
"""
result = [[0 for _ in range(l)]for _ in range(n)]

for _ in range(n):
    A.append(list(map(int, input().split())))

for _ in range(m):
    B.append(list(map(int, input().split())))

for i in range(n):
    for j in range(l):
        for k in range(m):
            result[i][j] += A[i][k]*B[k][j]


for i in result:
    print(*i)