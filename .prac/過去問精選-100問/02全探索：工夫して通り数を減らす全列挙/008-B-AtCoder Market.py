#全部関数内に入れて実行時に呼び出し

def main():
    import sys
    def input():
        return sys.stdin.readline().rstrip()
    
    N = int(input())#max 30
    A, B = 0,1
    sinamono = [list(map(int,input().split())) for _ in range(N)]
    
    min_total_time = float('inf')
    entrance = 0
    exit = 0
    for x in range(N): #N人の買い物客の商品のどこかからスタートとゴールを決める
        entrance = sinamono[x][A]
        for y in range(N):
            exit = sinamono[y][B]
            tmp_time = 0
            #口が決まったところでそれぞれ時間を計算
            for i in range(N):
                tmp_time += abs(sinamono[i][A]-entrance)+abs(sinamono[i][B]-sinamono[i][A])+abs(exit-sinamono[i][B])
            if min_total_time > tmp_time:
                min_total_time = tmp_time
    print(min_total_time)

#全部関数内に入れて実行時に呼び出し-2
if __name__ == '__main__':
    main()