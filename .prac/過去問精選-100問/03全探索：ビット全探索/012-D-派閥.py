# D-派閥 https://atcoder.jp/contests/abc002/tasks/abc002_4
def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    
    # 整数複数個
    N, M = map(int, input().split())

    # 整数 (縦 N 横 W の行列)
    relation = set()
    for _ in range(M):
        relation.add(tuple(map(int, input().split())))

    result = 0

    for bit in range(1<<N):
        members = []
        for i in range(N):
            if (bit & (1<<i)) == (1<<i):
                flag_append = True
                if members == []:
                    pass
                else:
                    for m in members:
                        if ((i+1,m+1) not in relation) and ((m+1,i+1) not in relation):
                            flag_append = False
                
                if flag_append:
                    members.append(i)
        
        if result < len(members):
            result = len(members)
        
    print(result)


if __name__ == '__main__':
    main()