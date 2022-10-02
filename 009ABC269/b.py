def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    
    # 整数 1 つ
    # N = int(input())
 
    # 整数複数個
    # N, K = map(int, input().split())
 
    # 整数 N 個 (改行区切り)
    ls = [input() for i in range(10)]
 
    # 整数 N 個 (スペース区切り)
    # A = list(map(int, input().split()))
 
    # 整数 (縦 N 横 W の行列)
    # S = [list(map(int, input().split())) for _ in range(N)]
    a = 0
    b = 0
    c = 0
    d = 0
    for i,s  in enumerate(ls):
        if ("#" in s) and a==0:
            a = i+1
        elif a!=0 and b==0 and ("#" not in s):
            b = i
    
    if a!=0 and b==0:
        b=10

        
    for j,moji in enumerate(ls[a-1]):
        if c==0 and (moji=="#"):
            c = j+1
        elif c!=0 and d==0 and (moji!="#"):
            d = j
    if c!=0 and d==0:
        d=10
    
    print(a, b)
    print(c, d)



if __name__ == '__main__':
    main()