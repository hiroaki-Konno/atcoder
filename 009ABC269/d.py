def main():
    import sys
    import numpy as np

    def input():
        return sys.stdin.readline().rstrip()
    
    # 整数 1 つ
    N = int(input())
 
    # 整数複数個
    masu = sorted([list(map(int, input().split())) for i in range(N)])

    masu = np.array(masu)-masu[0]
    print(masu)

    xmax = np.amax(masu, axis=0)
    ymax = np.amax(masu, axis=1)
    print(xmax, ymax)

    mapls = [[0] * xmax[0] for i in range(ymax[len(ymax)]+1)]
    print(mapls)

    result = len(masu)

    for n, e in enumerate(masu):
        x, y = e[0], e[1]
        mapls[x][y]=1
        if n == 0:
            pass
        if mapls[x-1][y-1] or mapls[x-1][y] or mapls[x][y-1]:
            result -= 1
        if mapls[x-1][y] and mapls[x][y-1] and not mapls[x-1][y-1]:
            result -= 1
        
    print(result)


if __name__ == '__main__':
    main()