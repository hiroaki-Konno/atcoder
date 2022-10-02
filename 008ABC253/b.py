def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()

    # 整数複数個
    H, W = map(int, input().split())

    # 整数 (縦 H 横 W の行列)
    S = [input() for i in range(H)]

    two_points = []
    for i in range(H):
        for j in range(W):
            if S[i][j] == "o":
                two_points.append([i, j])
    
    dis = abs(two_points[0][0]-two_points[1][0]) + abs(two_points[0][1]-two_points[1][1])
    print(dis)


if __name__ == '__main__':
    main()