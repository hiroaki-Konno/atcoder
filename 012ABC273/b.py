def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    
    # 整数 1 つ
    # N = int(input())
 
    # 整数複数個
    X, K = map(int, input().split())
 
    # 整数 N 個 (改行区切り)
    # L = [int(input()) for i in range(N)]
 
    # 整数 N 個 (スペース区切り)
    # A = list(map(int, input().split()))
 
    # 整数 (縦 N 横 複数 の行列)
    # S = [list(map(int, input().split())) for _ in range(N)]

    for i in range(1,K+1):
        teni = 10**i
        if X%teni >= 5*(teni//10):
            X = (X//teni+1)*teni
        else:
            X = (X//teni)*teni
    print(X)

if __name__ == '__main__':
    main()