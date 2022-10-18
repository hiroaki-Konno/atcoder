def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    
    def dprint(*arr, end="\n", sep=" "):
        # return
        if sys.argv[-1]=="DEBUG":
            print("DEBUG:",*arr, end=end, sep=sep)
    
    # 整数 1 つ
    N = int(input())

    # 整数複数個
    S = list(map(int, input().split()))

    # 整数 1 つ
    q = int(input())

    # 整数複数個
    T = list(map(int, input().split()))

    result = 0

    def binary_search(S, key):
        """
        keyが見つかったらS内でのindexを返す
        見つからなかったら-1を返す
        """
        left = 0
        right = N #(len(S))
        while left < right:
            mid = (left+right)//2
            if S[mid]==key:
                return mid
            elif key < S[mid]:
                right = mid
            else:
                left = mid+1
        return -1

    for ti in T:
        if binary_search(S, ti) != -1:
            result += 1
        # 新しく配列作るよりも添え字の操作した方が早い
        # list[index]のアクセスはO(1)なので使い得
        """
        # 偶数の場合真ん中二つのうち大きい方になる
        #pivot = N//2 
        tmp = S

        while True:
            pivot = len(tmp)//2
            if ti < tmp[pivot]:
                tmp = tmp[:pivot]
            
            elif ti == tmp[pivot]:
                result += 1
                break
        
            else:
                tmp = tmp[pivot:]
            
            if len(tmp)==1 and ti!=tmp[0]:
                break
        """

    print(result)

if __name__ == '__main__':
    main()