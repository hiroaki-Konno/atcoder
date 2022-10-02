def main():
    import sys
    def input():
        return sys.stdin.readline().rstrip()
    W = int(input())
    N = 0
    A = []

    MAX_N = 30
    fib = [None] * (MAX_N + 1)  # 計算結果を保存する配列
    fib[0] = 0  # 定義より
    fib[1] = 1  # 定義より

    rest_list = list(range(1,W+1))
    def getfib(n):
        # フィボナッチ数を2からnまで順に求めていく
        for i in range(2, n + 1):
            fib[i] = fib[i-1] + fib[i-2]
        return fib[n]
    #fib埋める
    getfib(MAX_N)
    A = fib[1:]

    def geti(num):
        i = 0
        while num > fib[i]:
            i+=1
        return i

    for num in list(range(1,W+1))[::-1]:
        #iをnum直前のfibの添え字に
        i = geti(W)
        nokori = (num - fib[i] - fib[i-2])
        if nokori > 0 and nokori not in A:
            A.append(nokori)


            
    N = len(A)
    print(N)
    print(*A)
if __name__ == '__main__':
    main()