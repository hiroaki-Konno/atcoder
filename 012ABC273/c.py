def main():
    import sys
    import collections

    def input():
        return sys.stdin.readline().rstrip()
    
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

    Asort = sorted(list(set(A)))

    #A = sorted(A)

    #print(Asort)
    #[1, 2, 7, 8]

    length = len(Asort)

    c2 = collections.Counter(A)
    result = []
    for i, num in enumerate(Asort):
        count = c2[num]
        result += count*[length-i-1]
            
    """ 
    count = 0
    for c, num in enumerate(Asort):
        for ai in A[count:]:
            if num == ai:
                result.append(length-c-1)
                count += 1
            else:
                break """
    
    c = collections.Counter(result)

    #print("c[0]",c[0])
    for i in range(N):
        print(c[i])


if __name__ == '__main__':
    main()