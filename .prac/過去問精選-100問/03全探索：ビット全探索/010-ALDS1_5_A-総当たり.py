def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    
    # 整数 1 つ
    n = int(input())
    
    # 整数 N 個 (スペース区切り)
    A = list(map(int, input().split()))

    # 整数 1 つ
    q = int(input())

    # 整数 N 個 (スペース区切り)
    mi = list(map(int, input().split()))

    #作れる数を辞書に格納
    flag = {}

    for binary in range(1<<n): #1<<n(n=20) = 1048576
        tmp = 0
        for index in range(n): #n=20
            if (binary & (1<<index)): #==1なら
                tmp += A[index]
            #作った数を辞書に格納
            flag[tmp] = True
    
    for m in mi:
        #添え字で検索、存在するなら...
        if m in flag:
            print("yes")
        else:
            print("no")
if __name__ == '__main__':
    main()


""" 
def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    
    # 整数 1 つ
    n = int(input())
    
    # 整数 N 個 (スペース区切り)
    A = list(map(int, input().split()))

    # 整数 1 つ
    q = int(input())

    # 整数 N 個 (スペース区切り)
    mi = list(map(int, input().split()))
    for i in range(q): #q=200
        ismi = False
        for binary in range(1<<n): #1<<n(n=20) = 1048576
            tmp = 0
            for index in range(n): #n=20
                if (binary & (1<<index)): #==1なら
                    tmp += A[index]
            if tmp == mi[i]:
                ismi = True
                break
        if ismi:
            print("yes")
        else:
            print("no")
if __name__ == '__main__':
    main()

 """