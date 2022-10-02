import collections
from typing import Counter


def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    
    # 整数 1 つ
    N = int(input())

    # 整数 N 個 (スペース区切り)
    A = list(map(int, input().split()))
    A_set = set(A)

    result = N * (N-1) * (N-2) // 6

    count = collections.Counter(A)
    print(count)
    minus = 0

    for ai in A_set:
        num = count[ai]
        if num != 1:
            result -= 
    
    if minus != 1:
        result -= minus
    print(result)

    


if __name__ == '__main__':
    main()