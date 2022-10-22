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
    # N = int(input())
 
    # 整数複数個
    H, W = map(int, input().split())
 
    # 整数 N 個 (改行区切り)
    # L = [int(input()) for i in range(N)]
 
    # 整数 N 個 (スペース区切り)
    # A = list(map(int, input().split()))
 
    # 整数 (縦 N 横 複数 の行列)
    C = [input() for _ in range(H)]

    result = [0]*W

    for Ciw in C:
        for i in range(W):
            if Ciw[i] == "#":
                result[i]+=1
    
    print(*result)

if __name__ == '__main__':
    main()