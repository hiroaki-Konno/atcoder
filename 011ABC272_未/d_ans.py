def main():
    """ https://qiita.com/MoroeTachibana-oh/items/2128746896925fbaac5c#1-5-d%E5%95%8F%E9%A1%8C-root-m-leaper より """
    import sys
    from collections import deque

    def input():
        return sys.stdin.readline().rstrip()

    # 整数 1 つ
    # N = int(input())

    # 整数複数個
    N, M = map(int, input().split())

    # 一回の操作でどこへ移動させられるか
    able = []

    for i in range(int(M**0.5) + 1):
        n = M - i**2
        if n < 0:
            break
        n = n**0.5
        if int(n) == n:
            n = int(n)
            able.append((i, n))
            able.append((i, -n))
            able.append((-i, n))
            able.append((-i, -n))
            able.append((i, n))
            able.append((i, -n))
            able.append((-i, n))
            able.append((-i, -n))

    # 始点になる座標の管理用キュー
    D = deque()
    D.append([0, 0])

    # 移動回数保存用の配列 初期値は-1
    result = [[-1]*N for _ in range(N)]
    result[0][0] = 0

    # 条件判定用の関数 無名関数だとこう書くらしい
    # ok = lambda x, y: 0 <= x < N and 0 <= y < N and result[x][y] == -1
    def ok(x, y):
        """ 座標が範囲内かつ移動回数が設定されていないか判定 """
        if (0<=x<N) and (0<=y<N) and (result[x][y]==-1):
            return True
        return False
    
    # 座標が更新された点を始点として更新
    # (更新された＆始点になってない)点がなくなるまで繰り返し
    while D:
        x, y = D.popleft()
        for a, b in able:
            # 移動後の座標
            nx, ny = x + a, y + b
            # 更新条件に当てはまるか判断
            if not ok(nx, ny):
                continue
            # 始点の移動回数 + 1を代入
            result[nx][ny] = result[x][y] + 1
            # 更新された点を追加
            D.append([nx, ny])
    
    # 結果を表示
    for n in result:
        print(*n, sep=" ")


if __name__ == '__main__':
    main()