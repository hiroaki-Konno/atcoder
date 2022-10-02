def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()

    # 整数 1 つ
    N = int(input())
 
    # 整数複数個
    # N, K = map(int, input().split())
 
    # 整数 N 個 (改行区切り)
    # L = [int(input()) for i in range(N)]
 
    # 整数 N 個 (スペース区切り)
    # A = list(map(int, input().split()))
 
    # 整数 (縦 N 横 W の行列)
    # S = [list(map(int, input().split())) for _ in range(N)]

    cmb_ls=[]
    result = set()
    n_bin = bin(N)
    # print("n_bin", n_bin)
    for i, num in enumerate(reversed(n_bin[2:])):
        # print(num)
        if num=='1':
            cmb_ls.append(2**i)
    
    # print("cmbls", cmb_ls)

    for j in range(2**len(cmb_ls)):
        tmp = 0
        for k in range(len(cmb_ls)):
            if j & (1<<k):
                tmp += cmb_ls[k]
        result.add(tmp)
    
    print(*result, sep="\n")

if __name__ == '__main__':
    main()