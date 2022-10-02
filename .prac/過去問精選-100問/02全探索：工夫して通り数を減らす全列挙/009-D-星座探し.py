from ntpath import realpath


def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    
    # 整数 1 つ
    N = int(input())
    N_list = [list(map(int, input().split())) for _ in range(N)]

    M = int(input())
    M_list = sorted([list(map(int, input().split())) for _ in range(M)])

    relative_pos = [[N_list[i][0]-N_list[0][0], N_list[i][1]-N_list[0][1]] for i in range(N)]

    #それぞれ星を星座の基準の星にあてはめる
    for star in M_list:
        for num, pos in enumerate(relative_pos):
            #基準から相対化した座標を足してそれぞれの実座標を得る
            next_star_x, next_star_y = star[0]+pos[0], star[1]+pos[1]

            #値がマイナスだったらbreak
            if  not (next_star_x > 0) and (next_star_y > 0):
                break

            #値が存在するかどうかチェックしていく
            exist_star = False
            for s in M_list:
                if s[0] > next_star_x:
                    break
                if (s[0] == next_star_x) and (s[1] == next_star_y):
                    exist_star = True
                    break

            #星が存在しなければ基準の星を変更
            if  not exist_star:
                break

            #全部見つかった()
            if num == N-1:
                #star(基準)と星座の一つ目n_list[0]を比較
                print(star[0]-N_list[0][0], star[1]-N_list[0][1])
if __name__ == '__main__':
    main()