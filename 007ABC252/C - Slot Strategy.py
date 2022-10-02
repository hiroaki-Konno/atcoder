def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    
    # 整数 1 つ
    N = int(input())

    # 整数 N 個 (改行区切り)
    S = [input() for i in range(N)]


    result = 100000000000


    #そろえる数字決める
    for i in range(10):
        sec = 0
        #i = 8
        isstoped = [0]*N
        fin = False

        while not fin:
            for si, s in enumerate(S):
                #止まってるリールならスキップ
                if isstoped[si] == 1:
                    continue

                #それぞれリールの状況再現
                tmp_sec = sec % 10
                tmp_s = s[tmp_sec:] + s[:tmp_sec]

                #現状のリールが止めたい数字なら
                if int(tmp_s[0]) == i:
                    #停止したことを記録
                    isstoped[si] = 1

                    #全部止まってるかの確認
                    if min(isstoped) == 1:
                        #止まってるなら終了
                        fin = True
                    break
            if fin:
                break
            #次の秒へ移行
            sec += 1
        #for debug
        #print("i:", i, sec)

        if result > sec:
            result = sec
    
    print(result)
            
if __name__ == '__main__':
    main()