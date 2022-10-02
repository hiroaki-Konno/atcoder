def main():
    import sys
    from collections import defaultdict

    def input():
        return sys.stdin.readline().rstrip()

    N = int(input())
    ST = defaultdict(list)
    #ST = [[txt(S),score(T), index]]
    max_original_score = 0
    max_original_index = 0
    for index in range(N):
        s, t = input().split()
        if ST[s] == []:
            ST[s] = [int(t), index]
        if max_original_score < ST[s][0]:
            max_original_score = ST[s][0]
            max_original_index = ST[s][1]
    
    print(max_original_index+1)
    #print(ST)
if __name__ == '__main__':
    main()