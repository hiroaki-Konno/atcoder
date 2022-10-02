#圧倒的未完成






#mapのサイズ
SIZE = 30

#最後にprintする文字列
result = "0"*900
tmp_result = result

#タイルの状態が入った二次元配列tiles
#文字列のままなので適宜int変換
tiles = []
for _ in range(SIZE):
    tiles.append(list(map(int, list(input()))))


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

""" class Tile:
    def __init__(self, type):
        self.type = type
        self.rotate = 0
        self.to = to[type]
    
    def rotate(self):
        self.rotate += 1 """

#最初のところにふさわしいかの判定と回転
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

#見つかったかの条件変数
is_found = [0] * 4 #左上から時計回り0->1->2->3
found_point = [0,0]

#左上探す
for i in range(0, SIZE//2):
    #左三列探す
    for j in range(3):
        #適するかのチェック
        if check_start_tile(i, j):
            """ 満たすなら条件変数 1に """
            is_found[0] = 1
            found_point = [i,j]
            break
    #見つかったらbreak
    if is_found[0] == 1:
        break


#一つ目の周(上)(縦iがSIZE//2まで)
#最初の点から始める
for i in range(found_point[0], SIZE//2):
    #found?pointの右隣から
    for j in range(found_point[1]+1, SIZE):
        d_next = to[tiles[i][j]][]
        ttype = tiles[i][j]
        if to[ttype][0] == -1:
            if ttype < 4:
                if ttype == 0:
                    to[ttype][to[ttype][0]]
        
        


#二つ目の周(下)
for i in range(SIZE//2, SIZE):
    for j in range(SIZE)
