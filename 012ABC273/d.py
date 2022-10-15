def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    
 
    # 整数複数個
    H, W, rs, cs = map(int, input().split())

    # 整数 1 つ
    N = int(input())
 
    # 整数 (縦 N 横 複数 の行列)
    r = [(map(int, input().split())) for _ in range(N)]
 
    # 整数 1 つ
    Q = int(input())

    # 整数 (縦 Q 横 複数 の行列)
    d = [list(input().split()) for _ in range(Q)]

    """ rは壁 Qは指示(上下左右と移動距離、ただし壁にはつっかかる) """

    #field = [[0]*W for _ in range(H)]

    def can_move(tate, yoko):
        if (tate<1) or (H<tate) or (yoko<1) or (W<yoko):
            return False
        if (tate, yoko) in r:
            return False
        return True

    def move(muki, distance, now_pos):
        """ 移動方向、移動距離、現在位置 """
        tate, yoko = now_pos
        for i in range(distance):
            if muki == "L":
                if can_move(tate, yoko-1):
                    yoko -= 1
                else:
                    break
            elif muki == "R":
                if can_move(tate, yoko+1):
                    yoko += 1
                else:
                    break
            elif muki == "U":
                if can_move(tate-1, yoko):
                    tate -= 1
                else:
                    break
            elif muki == "D":
                if can_move(tate+1, yoko):
                    tate += 1
                else:
                    break
        now_pos = (tate, yoko)
        return now_pos

    #print(H,W, rs, cs, N, Q, d, sep="\n")

    now_pos = (rs, cs)
    for di in d:
        now_pos = move(di[0], int(di[1]), now_pos)
        print(*now_pos)

if __name__ == '__main__':
    main()