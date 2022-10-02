N, M = map(int, input().split())

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

ans = 0

for j in range(M):
    for k in range(j,M):#j, k曲目を使用
        tmp = 0
        for i in range(N):#i人目
            tmp += max(A[i][j],A[i][k])
        if ans < tmp:
            ans = tmp

print(ans)