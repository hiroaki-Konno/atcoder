def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    
    # 整数 1 つ
    N = int(input())

    # 整数 N 個 (改行区切り)
    S = [input() for i in range(N)]


    result = 100000000000
    #数字決める
    #for i in range(10):
    i = 8
    now_sec = 0
    isstoped = [0]*N
    fin = False

    loops = 0
    prev_j = -1
    #桁数決める
    while not fin:
        for j in range(10):
            next = False
            #for si, s in enumerate(S):
            si = 0
            sec = 0
            while (not next) and (sec < 10) and (N > si):
                s = S[si]
                #停止してたらスキップ
                if isstoped[si] == 1:
                    si += 1
                    continue
                if int(s[j]) == i:
                    if prev_j >= j:
                        isstoped[si] = 1
                        next = True
                        si += 1
                        break
                    #停止したことを記録
                    isstoped[si] = 1
                    now_sec = j
                    sec += j
                    prev_j = j
                si += 1
            if min(isstoped) == 1:
                fin = True
            
            if next:
                break
        loops += 1

    now_sec = (loops)*10 + now_sec
    if result > now_sec:
        result = now_sec
    
    print(result)
            
if __name__ == '__main__':
    main()