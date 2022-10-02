def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    
    # 整数複数個
    N, K = map(int, input().split())
    # 整数 1 つ
    S = list(input())

    changed_S_list = [[[[0]*K] * 26 for _ in range(K+1)] for _ in range(K+1)]

    changed_S_list[0][1][0] = S
    min_fs = N

    tmp = set()

    for j in range(N):
        txt = "".join(S[j:]+S[:j])
        if txt not in tmp:
            tmp.add(txt)
    if min_fs > len(tmp):
        min_fs = len(tmp)

    for i in range(0,K+1):#0,1,2...,K回以下実行
        tmp = set()
        for j in range(1,K+1):
            for k in range(0,K+1):
                S = changed_S_list[i][j][k]
                for l in range(N):#SのL文字目を変換
                    for s in range(26):#L文字目をアルファベットs番目に変換
                        tmp_l = set()
                        S[l] = chr(97+s)
                        changed_S_list[i][l][s] = S
                        #f(S)を評価
                        for j in range(N):
                            txt = "".join(S[j:]+S[:j])
                            if txt not in tmp_l:
                                tmp_l.add(txt)
                        if min_fs > len(tmp_l):
                            min_fs = len(tmp_l)
        
            
    print(min_fs)

if __name__ == '__main__':
    main()