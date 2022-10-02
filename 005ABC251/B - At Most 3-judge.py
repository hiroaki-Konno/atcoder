def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    N, W = map(int,input().split())
    A = list(map(int, input().split()))
    n_set = set()

    for i in range(N):
        tmp_i = 0
        tmp_i += A[i]
        if tmp_i <= W:
            n_set.add(tmp_i)
        for j in range(i+1, N):
            tmp_j = tmp_i
            tmp_j += A[j]
            if tmp_j <= W:
                n_set.add(tmp_j)
            for k in range(j+1, N):
                tmp_k = tmp_j
                tmp_k += A[k]
                if tmp_k <= W:
                    n_set.add(tmp_k)
    print(len(n_set))
    #print(n_set)


#全部関数内に入れて実行時に呼び出し-2
if __name__ == '__main__':
    main()