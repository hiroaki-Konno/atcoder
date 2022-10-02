import collections


def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    
    # 整数 1 つ
    Q = int(input())

    # 整数 (縦 N 横 W の行列)
    querry = [list(map(int, input().split())) for _ in range(Q)]

    S = []
    num_set = set()
    counter = dict()

    for qi in querry:
        if qi[0] == 1:
            x = str(qi[1])
            try:
                counter[x]
            except:
                counter[x] = 0
            counter[x] += 1

        elif qi[0] == 2:
            x = str(qi[1])
            c = qi[2]
            if c > counter[x]:
                #roops = counter[x]
                counter[x] = 0
            else:
                #roops = c
                counter[x] -= c
            
            """ for _ in range(roops):
                S.remove(x) """
            
        elif qi[0] == 3:
            print(list(counter)[len(list(counter))-1]-list(counter)[0])
        counter = sorted(counter.items(), key=lambda x:x[0])
    #print(S)

if __name__ == '__main__':
    main()