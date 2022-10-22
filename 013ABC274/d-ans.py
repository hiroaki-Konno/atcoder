def main():
    """
    解説をコードに起こしたら動くといいなと思う
    解説: https://atcoder.jp/contests/abc274/editorial/5079
    参考にした解答: https://atcoder.jp/contests/abc274/submissions/35902936
    """
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

    A_max = 10
    # Aの最大値がN個並んだ時も格納できるdpを作成する
    # 最大値*個数でありうる絶対値が出せる
    M = A_max*N


    """ 
    # 1次元の場合
    # 正負それぞれ Mが最大、に足して0の分なので
    # -M ~ 0 ~ M で 2*M + 1 
    dp = [False]*(2*M + 1)

    # 座標でいうところの0の値をTrueに
    dp[M] = True
    

    # 与えられたAに対してdpを更新していく
    for i in range(N):
        next_dp = [False]*(2*M + 1)
        for j in range(-M, M+1):
            # -Mスタートなのでその分ずらす
            if dp[j+M]:
                # 現在地から入力されただけ右に移動したところにマーク
                next_dp[j+M+A[i]] = True

                # 0番目のみ右に出す制約があるので分岐
                if i > 0:
                    # 現在地から入力されただけ左に移動したところにマーク
                        next_dp[j+M-A[i]] = True
        dp = next_dp

    if dp[x+M] == True:
        print("Yes")
    else:
        print("No")
    """
    
    # 2次元の場合
    # x, y の正負それぞれ最大の絶対値が M、それに足して0の分なので
    # -M ~ 0 ~ M で 2*M + 1 
    dp_x = [False]*(2*M + 1)
    dp_y = [False]*(2*M + 1)

    # 座標でいうところの0の値をTrueに 
    # (0, 0) = True
    dp_x[M] = True
    dp_y[M] = True
    

    # 与えられたAに対してdpを更新していく
    for i in range(N):
        next_dp = [False]*(2*M + 1)
        # 横の場合
        if (i%2 ==0):
            for j in range(-M, M+1):
                # -Mスタートなのでその分ずらす
                if dp_x[j+M]:
                    # 現在地から入力されただけ右に移動したところにマーク
                    next_dp[j+M+A[i]] = True

                    # 0番目のみ右に出す制約があるので分岐
                    if i > 0:
                        # 現在地から入力されただけ左に移動したところにマーク
                            next_dp[j+M-A[i]] = True
            dp_x = next_dp
        # 縦の場合
        else:
            for j in range(-M, M+1):
                # -Mスタートなのでその分ずらす
                if dp_y[j+M]:
                    # 入力されただけ上にマーク
                    next_dp[j+M+A[i]] = True

                    # 入力されただけ下にマーク
                    next_dp[j+M-A[i]] = True
            dp_y = next_dp

    if (dp_x[x+M] == True) and (dp_y[y+M] == True):
        print("Yes")
    else:
        print("No")
   



if __name__ == '__main__':
    main()
