def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    
    # 整数複数個
    N, K = map(int, input().split())

    # 整数 N 個 (スペース区切り)
    A = list(map(int, input().split()))

    # 整数 N 個 (スペース区切り)
    B = list(map(int, input().split()))

    max_oisii = max(A)
    flag = False
    for b in B:
        if max_oisii == A[b-1]:
            flag = True
            break

    if flag:
        print("Yes")
    else:
        print("No")
        


if __name__ == '__main__':
    main()