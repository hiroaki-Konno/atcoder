def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()

    def dprint(*arr, end="\n", sep=" "):
        # return
        #if sys.argv[-1]=="DEBUG":
        if sys.argv[-1]=="debug":
            print("DEBUG:",*arr, end=end, sep=sep)
    
    # ファイル実行時、末尾に DEBUGを付けて実行するとprintされる
    # dprint("debug test")
 
    # 整数複数個
    N, x, y = map(int, input().split())
 
    # 整数 N 個 (スペース区切り)
    A = list(map(int, input().split()))

    #N回の移動で存在できる点を格納
    can_visit = [[] for _ in range(N)]

    now_pos = [A[0], 0]
    can_visit[0].append(now_pos)


    for i, ai in enumerate(A):
        if i == 0: continue

        for p in can_visit[i-1]:
            if i % 2 == 1:
                # 上
                can_visit[i].append([p[0], p[1]+ai])
                # 下
                can_visit[i].append([p[0], p[1]-ai])
            else:
                # 左
                can_visit[i].append([p[0]-ai, p[1]])
                # 右
                can_visit[i].append([p[0]+ai, p[1]])


    can_put = [x,y] in can_visit[N-1]

    if can_put:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
