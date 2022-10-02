def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    
    # 整数 1 つ
    # N = int(input())
 
    # 整数複数個
    N, S = map(int, input().split())
 
    # 整数 N 個 (改行区切り)
    # L = [int(input()) for i in range(N)]
 
    # 整数 N 個 (スペース区切り)
    # A = list(map(int, input().split()))
 
    # 整数 (縦 N 横 W の行列)
    AB = [list(map(int, input().split())) for _ in range(N)]
    
    # 重さSのナップサック問題 (N * S)
    """ 
    dp[i][j]:= カード 1,…,i のみを考えたとき、
              和を j にできるなら 1、そうでないなら 0 
    """
    dp = [[0]*(S+1) for _ in range(N+1)]

    dp[0][0] = 1

    # print(*dp, sep="\n")

    for i in range(N):
        # 表裏カードの値
        a, b = AB[i]
        for j in range(S):
            if dp[i][j]:
                if (j+a) <= S:
                    dp[i+1][j+a] = 1
                if (j+b) <= S:
                    dp[i+1][j+b] = 1
    
    #print("Yes" if dp[-1][-1]==1 else "No")

    if dp[-1][-1]==1:
        print("Yes")
        result = ""
        posj = S
        for i in range(N-1, -1, -1): # n=3 -> 2, 1, 0
            a, b = AB[i]
            if dp[i][posj-a]:
                posj -= a
                result += "H"
            elif dp[i][posj-b]:
                posj -= b
                result += "T"

        print(result[::-1])

    else:
        print("No")
    
    #print(*dp, sep="\n")
    #print(dp[-1])

if __name__ == '__main__':
    main()