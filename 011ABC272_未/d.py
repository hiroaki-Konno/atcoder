def main():
    """ いくつかACは出るものの正解には至らず """
    import sys
    import itertools
    debug = print
    def input():
        return sys.stdin.readline().rstrip()
    
    # 整数 1 つ
    # N = int(input())
 
    # 整数複数個
    N, M = map(int, input().split())
 
    # 整数 N 個 (改行区切り)
    # L = [int(input()) for i in range(N)]
 
    # 整数 N 個 (スペース区切り)
    # A = list(map(int, input().split()))
 
    # 整数 (縦 N 横 複数 の行列)
    # S = [list(map(int, input().split())) for _ in range(N)]

    result = [[-1]*N for _ in range(N)]

    move_xy_diff = []

    point_xy = [[(0, 0)]]
    count = 1

    # 移動幅 move_xy 求める
    """ 
    for y in range(N):
        for x in range(N):
    """
    for iter in itertools.combinations(range(N), 2):
        x, y = iter
        # 移動幅が Mちょうど
        if (x**2+y**2)==M:
            move_xy_diff = [x, y]
            point_xy.append([])

            result[x][y] = count
            # 1にした点 append
            point_xy[count].append((x,y))

            # もう一方の点更新 append
            result[y][x] = count
            point_xy[count].append((y,x))

            break
    # point_xy = [
    #       [(0,0)],
    #       [(x,y), (y,x)],
    # ]

    """ うまくいった """
    #debug(point_xy)

    x, y = move_xy_diff
    moves = [(x,y), (x,-y), (-x,y), (-x,-y), (y,x), (y,-x), (-y,x), (-y,-x)]
    is_updated = True

    while is_updated:
        is_updated = False
        # 値==countの座標を保存する配列追加
        point_xy.append([])
        point_xy_count = point_xy[count]
        count += 1
        # 追加された点 p for 
        for p in point_xy_count:
            px , py = p
            # pから移動幅分ずらして(最大8通り)
            for move in moves:
                tmpx = px + move[0]
                tmpy = py + move[1]
                
                # 範囲内に収まる and 値が入ってない 
                if (0<=tmpx) and (tmpx<N) and (0<=tmpy) and (tmpy<N) and (result[tmpx][tmpy]==-1):
                    #debug(tmpx,tmpy)
                    if (tmpx, tmpy) == (0,0):
                        result[tmpx][tmpy] = 0
                        continue
                    # pの値+1代入
                    result[tmpx][tmpy] = count
                    # append
                    point_xy[count].append((tmpx, tmpy))
                    is_updated = True
    

    [print(*rt) for rt in result]
          

    

if __name__ == '__main__':
    main()