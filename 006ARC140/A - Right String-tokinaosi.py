""" def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    
    # 整数複数個
    N, K = map(int, input().split())
    # 整数 1 つ
    S = list(input())

    result = N
    for M in range(1,N):
        if N % M != 0:
            continue


if __name__ == '__main__':
    main()

 """

#koroshoさん https://atcoder.jp/contests/arc140/submissions/31740474
from collections import Counter
N,K = map(int,input().split())
S = input()

#print("---")
 
for d in range(1,N//2+1):
    if N % d != 0: continue
    s = 0
    #print("width:", N//d, "d:", d)
    #幅Dで区切る(繰り返す)
    for i in range(d):
        #幅Dのi文字目を全部取り出す...(1)
        #print(S[i::d])
        #print(Counter(S[i::d]))
        #print(Counter(S[i::d]).values())
        #(1)の中で一番多い文字に揃える前提で変更が何回されるか計算しsに加算
        s += N // d - max(Counter(S[i::d]).values()) 
    print()
    #変更可能な回数に収まるなら出力
    if s <= K: exit(print(d))
 
print(N)