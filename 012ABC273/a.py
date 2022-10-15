def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    
    # 整数 1 つ
    N = int(input())
 
    # 整数複数個
    # N, K = map(int, input().split())
 
    # 整数 N 個 (改行区切り)
    # L = [int(input()) for i in range(N)]
 
    # 整数 N 個 (スペース区切り)
    # A = list(map(int, input().split()))
 
    # 整数 (縦 N 横 複数 の行列)
    # S = [list(map(int, input().split())) for _ in range(N)]

    result = 1
    for i in range(1,N+1):
        result*= i

    print(result)
if __name__ == '__main__':
    main()