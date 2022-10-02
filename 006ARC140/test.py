def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    
    # 整数複数個
    N, K = map(int, input().split())
    # 整数 1 つ
    S = input()
    tmp_l = set()

    #f(S)を評価
    for j in range(N):
        if S[j:]+S[:j] not in tmp_l:
            tmp_l.add(S[j:]+S[:j])
    print(len(tmp_l))
if __name__ == '__main__':
    main()