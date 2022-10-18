def main():
    """ https://onlinejudge.u-aizu.ac.jp/solutions/problem/ALDS1_13_A/review/5899549/lloyz_nt/Python3 より """
    import sys
    from itertools import permutations
    from copy import copy

    def input():
        return sys.stdin.readline().rstrip()
    
    # 整数 1 つ
    k = int(input())


    # 整数 (縦 N 横 複数 の行列)
    rc = [list(map(int, input().split())) for _ in range(k)]

    # クイーンのいない行のリスト
    R = list(range(8))
    # クイーンのいない列のリスト
    C = list(range(8))

    # クイーンのいない右斜め(右上がり)のリスト
    pG = []
    # クイーンのいない左斜め(右下がり)のリスト
    mG = []
    # クイーンの位置のリスト
    Q = []

    for r, c in rc:
        # クイーンのいない行、列、斜めを更新
        R.remove(r)
        C.remove(c)
        pG.append(r + c) # 右上がり(和が一定)の斜め
        mG.append(r - c) # 右下がり(差が一定)の斜め
        # クイーンの位置を追加
        Q.append((r, c))
    # クイーンのいない行、列のマスに対し
    # クイーンを置く場所の組み合わせ全てのパターンを試す
    for RP in permutations(R):
        for CP in permutations(C):
            """
            RP [1, 2, 4, 5]
            CP [3, 7, 2, 1]
            RP, CPの添え字が同じ数字の組がクイーンの座標
            """
            pGc = copy(pG)
            mGc = copy(mG)
            flag = True
            # 各パターン斜めの組の計算(和と差)をして
            # 斜めにクイーンが存在しないか確認
            for ir, ic in zip(RP, CP):
                if ir + ic in pGc or ir - ic in mGc:
                    flag = False
                    break
                pGc.append(ir + ic)
                mGc.append(ir - ic)
            
            # 最期まで斜めの被りがなかった場合
            if flag:
                for ir, ic in zip(RP, CP):
                    Q.append((ir, ic))
                ans = [['.']*8 for _ in range(8)]
                for r, c in Q:
                    ans[r][c] = 'Q'
                for i in range(8):
                    print(''.join(ans[i]))
                exit()




if __name__ == '__main__':
    main()