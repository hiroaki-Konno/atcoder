#inにしたところACとTLEに #一番マシ
#https://atcoder.jp/contests/joi2007ho/submissions/31644353
def main():
    import sys
    def input():
        return sys.stdin.readline().rstrip()

    n = int(input())

    xys = []

    for i in range(n):
        xy = [int(t) for t in input().split()]
        xys.append(xy)

    max_area = 0
    x = 0
    y = 1
    #二点pi pj を取得して欲しい点があるか確認する
    for i in range(n):
        for j in range(i+1, n):
            xy_i_x, xy_i_y  = xys[i][x], xys[i][y]
            xy_j_x, xy_j_y  = xys[j][x], xys[j][y]

            #存在してほしい二点の座標を計算
            q = [xy_j_x-xy_j_y+xy_i_y, xy_j_y+xy_j_x-xy_i_x]
            r = [xy_i_x-xy_j_y+xy_i_y, xy_i_y+xy_j_x-xy_i_x]

            #inで存在を検索、あるなら最大面積を更新するか確認
            if [q[x],q[y]] in xys and [r[x], r[y]] in xys:
                if max_area  < (xy_i_x-xy_j_x)**2 + (xy_i_y-xy_j_y)**2:
                    max_area = (xy_i_x-xy_j_x)**2 + (xy_i_y-xy_j_y)**2

    print(max_area)

if __name__ == '__main__':
    main()