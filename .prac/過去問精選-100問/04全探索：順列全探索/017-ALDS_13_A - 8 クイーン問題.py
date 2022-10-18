def main():
    """ なんかちがうっぽい？？？ """
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    
    # 整数 1 つ
    k = int(input())

    # 整数 (縦 N 横 複数 の行列)
    rc = [list(map(int, input().split())) for _ in range(k)]

    can_put_queen = [1]*64

    def cross_update(pos, can_ls, width, up_or_down):
        """ 斜め四方向を幅とupdownで判断して更新 """
        stop_nums = {}
        jouhen = list(range(8))
        sahen = list(range(0,64,8))
        uhen = list(range(7,71,8))
        kahen = list(range(56,64))

        if width == 7:
            if up_or_down == "up":
                stop_nums = set(jouhen+uhen)
            elif up_or_down:
                stop_nums = set(kahen+sahen)
        if width == 9:
            if up_or_down == "up":
                stop_nums = set(jouhen+sahen)
            elif up_or_down:
                stop_nums = set(kahen+uhen)

        can_update = True
        tmp = pos
        while can_update:
            can_ls[tmp]=0
            tmp += width


    #与えられた点から可能性のない場所を更新
    for i in range(k):
        y, x = rc[i]
        puted_pos = y*8+x
        # 行(縦方向)の可能性つぶし
        can_put_queen[x::8] = [0]*8
        # 列(横方向)の可能性つぶし
        can_put_queen[8*y:8*(y+1)] = [0]*8
        # 右斜め
        can_put_queen[puted_pos%7::]
        # 左斜め

    print(*[can_put_queen[8*i:8*(i+1)] for i in range(8)], sep="\n")



if __name__ == '__main__':
    main()