def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    
    # 整数 1 つ
    # N = int(input())
 
    # 整数複数個
    N, Q = map(int, input().split())
 
    # 整数 N 個 (改行区切り)
    # L = [int(input()) for i in range(N)]
 
    # 整数 N 個 (スペース区切り)
    # A = list(map(int, input().split()))
 
    # 整数 (縦 N 横 W の行列)
    La = [list(map(int, input().split())) for _ in range(N)]

    sq = [list(map(int, input().split())) for _ in range(Q)]

    #print(La)
    #print("sq", sq)

    for i in range(Q):
        print(La[sq[i][0]-1][sq[i][1]])

if __name__ == '__main__':
    main()