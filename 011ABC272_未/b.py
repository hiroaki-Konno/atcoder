def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    
    # 整数 1 つ
    # N = int(input())
 
    # 整数複数個
    N, M = map(int, input().split())
 
    # 整数 N 個 (改行区切り)
    # L = [int(input()) for i in range(N)]
 
    # 整数 N 個 (スペース区切り)
    # A = list(map(int, input().split()))
 
    # 整数 (縦 N 横 複数 の行列)
    kx = [list(map(int, input().split())) for _ in range(M)]

    #print(kx)

    k = [kxi[0] for kxi in kx]
    x = [kxi[1:] for kxi in kx]

    is_friends = [[0]*N for _ in range(N)]

    for i, kxi in enumerate(kx):
        ki = kxi[0]
        xi = kxi[1:]
        for j, hito1 in enumerate(xi):
            hito1 -= 1
            for h, hito2 in enumerate(xi):
                hito2 -= 1
                is_friends[hito1][hito2] = 1
    
    min_is_friends = [min(i) for i in is_friends]

    if (min(min_is_friends)):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()