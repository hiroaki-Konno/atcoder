
N, K = map(int, input().split())

#降順で大きい要素を抜き出したリスト
A = reversed(list(range(N-K+1,N+1)))

baisuu = [0 for _ in range(N)]

result = 1
div = 1

for a in A:#降順 要素取り出し
    """ if baisuu[a] == 0:#倍数存在せず """
    for i in range(N):
        if baisuu[i] == 0:
            continue
        if a % i == 0:
            baisuu[i] = 1
        if sum(A) == len(A):
            #(N-(i+1)) C (K-(i+1))
            for j, e in enumerate(reversed(list(range(N-i)))):
                result *= e
                div *= j
                if (j == K-i):
                    result /= div


print(result%998244353)