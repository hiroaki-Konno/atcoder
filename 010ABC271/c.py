def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    
    # 整数 1 つ
    N = int(input())
 
    # 整数複数個
    A = list(map(int, input().split()))
 
    # 整数 N 個 (改行区切り)
    # L = [int(input()) for i in range(N)]
 
    # 整数 N 個 (スペース区切り)
    # A = list(map(int, input().split()))
 
    # 整数 (縦 N 横 W の行列)
    # S = [list(map(int, input().split())) for _ in range(N)]

    #print(N, A)
    A.sort()

    result = []
    count = 1 # 何巻までいった？
    pos = 0
    length = len(set(A)) # 被りなし
    kaburi = N - len(set(A))
    #print("kaburi", kaburi)

    A_no_kaburi = list(set(A))
    A_no_kaburi.sort()

    for i in range(N):
        if length <= 0:
            break
        if len(A_no_kaburi) > pos:
            ai = A_no_kaburi[pos]
        else:
            ai = -1
        if count == ai:
            result.append(ai)
            if kaburi <= 0:
                length -= 1
            else:
                kaburi -= 1
            pos += 1
            #print("if", length, kaburi)
        else:
            if length+kaburi >= 2:
                if kaburi >= 2:
                    kaburi -= 2
                elif kaburi == 1:
                    kaburi -= 1
                    length -= 1
                else:
                    length -= 2
                #print("else", length, kaburi)
                result.append(count)
            else:
                break
        count += 1
    
    #print(result, count)
    print(len(result))
if __name__ == '__main__':
    main()