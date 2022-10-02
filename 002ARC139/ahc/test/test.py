#mapのサイズ
SIZE = 30

#最後にprintする文字列
result = [0]*900
tmp_result = result

#タイルの状態が入った二次元配列tiles
#文字列のままなので適宜int変換
tiles = []
for _ in range(SIZE):
    #tiles.append(list(map(int, list(input()))))
    tiles.append(list(map(int, list("0" * SIZE))))

""" 状態 t 番のタイルに d の方向から侵入した際に次に向かうタイルの方向を to[t][d]、
ただしそのような方向から侵入不可能な場合は-1とする """
#方向を左上右下の順に0,1,2,3

to = [
    [1, 0, -1, -1],
    [3, -1, -1, 0],
    [-1, -1, 3, 2],
    [-1, 2, 1, -1],
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [2, -1, 0, -1],
    [-1, 3, -1, 1],
]
#縦の移動
di = [0, -1, 0, 1]
#横の移動
dj = [-1, 0, 1, 0]



def check_start_tile(i, j):
    t_type = int(tiles[i][j])
    ij = SIZE*i+j
    if t_type == 6 or t_type == 7:
        return False
    elif t_type == 0:
        tmp_result[ij] = 2
    elif t_type == 1:
        tmp_result[ij] = 3
    elif t_type == 2:
        pass
    elif t_type == 3:
        tmp_result[ij] = 1
    elif t_type == 4:
        pass
    elif t_type == 5:
        tmp_result[ij] = 1
    return True


def test_check_start_tile(num):
    t_type = num
    ij = 0
    if t_type == 6 or t_type == 7:
        return False
    elif t_type == 0:
        tmp_result[ij] = 2
    elif t_type == 1:
        tmp_result[ij] = 3
    elif t_type == 2:
        pass
    elif t_type == 3:
        tmp_result[ij] = 1
    elif t_type == 4:
        pass
    elif t_type == 5:
        tmp_result[ij] = 1
    return True

print(test_check_start_tile(4))
print(tmp_result[:5])

test_check_start_tile(6)
print(tmp_result[:5])

test_check_start_tile(1)
print(tmp_result[:5])