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
    
    # 整数 1 つ
    N = int(input())
 
    # 整数複数個
    # N, K = map(int, input().split())
 
    # 整数 N 個 (改行区切り)
    # L = [int(input()) for i in range(N)]
 
    # 整数 N 個 (スペース区切り)
    A = list(map(int, input().split()))
 
    # 整数 (縦 N 横 複数 の行列)
    # S = [list(map(int, input().split())) for _ in range(N)]

    nansedai = [0, 1, 1, 2, 2, 3, 3, 2, 2]
    nansedai = [0, 1, 1, 2, 2,]

    nansedai = [0]*(2*N + 1)

    for i, ai in enumerate(A):
        i += 1
        #長さ2を抜き出して代入 = 与えられた観察結果aiに一世代追加
        nansedai[2*i-1:2*i+1] = [nansedai[ai-1]+1]*2
    
    for i in nansedai:
        print(i)
    

    #print(result)
if __name__ == '__main__':
    main()