#全部関数内に入れて実行時に呼び出し
def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
        
    # 整数 1 つ
    N = int(input())

    # 整数複数個
    N, K = map(int, input().split())

    # 整数 N 個 (改行区切り)
    L = [int(input()) for i in range(N)]

    # 整数 N 個 (スペース区切り)
    A = list(map(int, input().split()))

    # 整数 (縦 H 横 W の行列)
    S = [list(map(int, input().split())) for _ in range(N)]
    
    
    n,m = 2,3
    #一次元リスト
    xs = [0] * n
    # 二次元リスト
    t = [[0] * m for _ in range(n)]


    INF = float('inf')

    #再帰できる回数の上限値
    sys.setrecursionlimit(10**6)


    #リストをスペース区切りで出力
    arr = [1, 2, 3]
    print(*arr)
    #リストを改行区切りで出力
    arr = [1, 2, 3]
    print(*arr, sep="\n")
    #最後に改行を入れない出力
    print("あああ", end="")

    

    #i 番目のアルファベットを整数 i に変換
    print(ord("a") - 97)
    #逆変換 
    print(chr(97 + 1)) #=="b"

    #辞書内包表記
    xys = {str(i): tuple(int(t) for t in input().split()) for i in range(n)}


    #処理の途中終了
    exit()


#全部関数内に入れて実行時に呼び出し-2
if __name__ == '__main__':
    main()

#python->TLEにならないループ回数は10の7乗回でした