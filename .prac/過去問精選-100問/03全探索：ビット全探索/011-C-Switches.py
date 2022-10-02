def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()

    N, M = map(int, input().split())

    ks = [list(map(int, input().split())) for i in range(M)]

    p = list(map(int, input().split()))

    result = 0
    for bit in range(1<<N):#N個のスイッチに対してbit全探索
        flag = True
        for m in range(M):
            tmp = 0
            for s in ks[m][1:]:
                #SのスイッチがONならば(添え字がずれてるから-1)
                if (bit & (1<<(s-1))):
                    tmp += 1
            if tmp % 2 != p[m]:
                flag = False
        if flag:
            result += 1

    print(result)
    
if __name__ == '__main__':
    main()