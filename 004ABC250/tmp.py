N, Q = map(int, input().split())
x = []
#番号格納用
ball_nums = [i for i in range(1,N+1)]
 
for _ in range(Q):
    x.append(int(input()))
 
for i in x:
    #.iindex()で多重ループなってたっぽい
    index = ball_nums.index(i)
    j = index + 1
    if index == N-1:
        j = index-1
    tmp = ball_nums[index]
    ball_nums[index] = ball_nums[j]
    ball_nums[j] = tmp
 
#print(x)
print(*ball_nums)