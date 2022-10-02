N, Q = map(int, input().split())
x = []
#番号格納用
ball_nums = [i for i in range(1,N+1)]

ball_indexes =  [i-1 for i in range(N+1)]

for _ in range(Q):
    x.append(int(input()))

for i in x:
    i_index = ball_indexes[i]
    if i_index == N-1:
        j_index = i_index-1
    else:
        j_index = i_index + 1
    tmp = ball_nums[i_index]
    ball_nums[i_index] = ball_nums[j_index]
    ball_nums[j_index] = tmp

    ball_indexes[i] = j_index
    ball_indexes[ball_nums[i_index]] = i_index


#print(x)
print(*ball_nums)