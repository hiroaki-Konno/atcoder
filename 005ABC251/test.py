MAX_N = 100
fib = [None] * (MAX_N + 1)  # 計算結果を保存する配列
fib[0] = 0  # 定義より
fib[1] = 1  # 定義より

def getfib(n):
    # フィボナッチ数を2からnまで順に求めていく
    for i in range(2, n + 1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

getfib(MAX_N)

print(fib)
print(10 ** 6)

from collections import deque


ls = list(range(5))
deque(ls)