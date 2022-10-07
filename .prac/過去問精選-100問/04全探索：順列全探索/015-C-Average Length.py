def main():
    import itertools
    import math
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    
    debug = print

    # 整数 1 つ
    N = int(input())

    # 整数 (縦 N 横 複数 の行列)
    xy = [list(map(int, input().split())) for _ in range(N)]
    
    total_dist = 0
    # N個のリストに対してN個選んだ順列を返すはず
    for iter in itertools.permutations(range(N)):
        #debug(iter)
        tmp_dist = 0
        for i in range(len(iter)-1):
            xi = xy[iter[i]][0]
            xj = xy[iter[i+1]][0]
            yi = xy[iter[i]][1]
            yj = xy[iter[i+1]][1]
            tmp_dist += ((xi-xj)**2+(yi-yj)**2)**0.5
        # debug(tmp_dist)
        total_dist += tmp_dist
    
    print(total_dist/math.factorial(N))
            

    
    
    #debug(N)
    #debug(xy)

if __name__ == '__main__':
    main()