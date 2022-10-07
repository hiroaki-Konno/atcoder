def main():
    import sys
    import itertools

    def input():
        return sys.stdin.readline().rstrip()
    
    # 整数 1 つ
    N = int(input())

    # 整数 N 個 (スペース区切り)
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    ap = 0
    bq = 0

    for c, iter in enumerate(itertools.permutations(range(1, N+1))):
        if list(iter) == P:
            ap = c
        if list(iter) == Q:
            bq = c


    print(abs(ap-bq))

if __name__ == '__main__':
    main()