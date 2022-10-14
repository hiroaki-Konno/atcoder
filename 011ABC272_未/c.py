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
    A = list(map(int, input().split()))
 
    # 整数 (縦 N 横 複数 の行列)
    # S = [list(map(int, input().split())) for _ in range(N)]

    # print(N)
    #print(A)
    A = list(reversed(sorted(A)))
    #print(A)

    max_evens = []
    max_odds = []

    for i in A:
        if (i%2) == 0:
            max_evens.append(i)
        else:
            max_odds.append(i)
        if (len(max_evens) == 2) or (len(max_odds) == 2):
            break
    
    if len(max_evens) == 2:
        print(sum(max_evens))
    elif len(max_odds) == 2:
        print(sum(max_odds))
    else:
        print(-1)


if __name__ == '__main__':
    main()