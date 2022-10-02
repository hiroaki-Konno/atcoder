#動くがRE, MLEまみれ
#https://atcoder.jp/contests/joi2007ho/submissions/me
def main():
    import sys
    def input():
        return sys.stdin.readline().rstrip()

    n = int(input())

    max_value = 5000
    bitmap = [[0] * (max_value+1) for _ in range(max_value+1)]
    xys = []

    for i in range(n):
        xy = [int(t) for t in input().split()]
        xys.append(xy)
        bitmap[xy[0]][xy[1]] = 1

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

            #bitmapから存在を検索、あるなら最大面積を更新するか確認
            if bitmap[q[x]][q[y]]==1 and bitmap[r[x]][r[y]]==1:
                if max_area  < (xy_i_x-xy_j_x)**2 + (xy_i_y-xy_j_y)**2:
                    max_area = (xy_i_x-xy_j_x)**2 + (xy_i_y-xy_j_y)**2

    print(max_area)

if __name__ == '__main__':
    main()