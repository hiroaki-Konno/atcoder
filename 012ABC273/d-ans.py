def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    
 
    # 整数複数個
    H, W, rs, cs = map(int, input().split())

    # 整数 1 つ
    N = int(input())
 
    # 整数 (縦 N 横 複数 の行列)
    rc = [(map(int, input().split())) for _ in range(N)]
 
    # 整数 1 つ
    Q = int(input())

    # 整数 (縦 Q 横 複数 の行列)
    dl = [list(input().split()) for _ in range(Q)]

    """ rcは壁 Qは指示(上下左右と移動距離、ただし壁にはつっかかる) """

    from bisect import bisect_left as bile
    # bisect_left
    # ソートされた順序を保ったまま x を a に挿入できる点を探し当てます。
    

    # i行目にある壁を昇順にした Ai
    # j列目にある壁を昇順にした Bj
    Ai, Bj = {}, {}  #Ai[x]はx行目、Bj[y]はy列目に存在する障害物
    rn, cn = set(), set()  #rn,cnは障害物の存在する行、列


    for r, c in rc:
        rn.add(r)
        cn.add(c)
        Ai.setdefault(r, [])
        Ai[r].append(c)
        Bj.setdefault(c, [])
        Bj[c].append(r)

    for i in Ai.keys():
        Ai[i].sort()
    for i in Bj.keys():
        Bj[i].sort()

    x, y = rs, cs  #現在地
    for i in dl:
        d = i[0]
        l = int(i[1])

        if d == "L":
            # 壁がなければとりあえず移動
            if x not in rn:
                y -= l
            # bile(二分法の関数)で yが挿入できるindexを求める、
            # 左方向への移動なので求めたindから 1 小さい数が
            # 最初に引っかかる壁のindexになる
            else:
                ind = bile(Ai[x], y) - 1
                if ind == -1:  #左に障害物がない
                    y -= l
                # 壁に引っかからなければ y-lが大きく、
                # 引っかかるなら最も近い壁の座標 Ai[x][ind]+1が大きく
                else:
                    y = max(y - l, Ai[x][ind] + 1)
        
        # Lとは足し引きの反転とmax minの反転
        elif d == "R":
            if x not in rn:
                y += l
            else:
                ind = bile(Ai[x], y)
                if ind == len(Ai[x]):  #右に障害物がない
                    y += l
                else:
                    y = min(y + l, Ai[x][ind] - 1)
        
        # 縦方向でLと同じことするだけ
        elif d == "U":
            if y not in cn:
                x -= l
            else:
                ind = bile(Bj[y], x) - 1
                if ind == -1:  #上に障害物がない
                    x -= l
                else:
                    x = max(x - l, Bj[y][ind] + 1)
        
        # 縦方向でRと同じことするだけ
        else:
            if y not in cn:
                x += l
            else:
                ind = bile(Bj[y], x)
                if ind == len(Bj[y]):  #下に障害物がない
                    x += l
                else:
                    x = min(x + l, Bj[y][ind] - 1)
        # とりあえずで移動させた分が範囲内に収まるようにする
        # マイナスの場合は1に、最大値超えるようならH(またはW)にする
        x = max(1, min(x, H))
        y = max(1, min(y, W))
        print(x, y)
    

if __name__ == '__main__':
    main()