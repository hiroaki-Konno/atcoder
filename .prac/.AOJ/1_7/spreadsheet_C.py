r, c = map(int, input().split())
result = [[] for _ in range(r+1)]

last_line = [0 for _ in range(c+1)]

for i in range(r):
    ls = list(map(int, input().split()))
    result[i] = ls + [sum(ls)]
    for j in range(c+1):
        last_line[j] += result[i][j]

result[r] = last_line
for l in result:
    print(*l)