import sys
#より高速に定義し直し
def input2():
    return sys.stdin.readline().rstrip()

n = int(input())
n2 = int(input2())
a = [list(map(int,input().split())) for _ in range(n)]
a2 = [list(map(int,input2().split())) for _ in range(n2)]

#それぞれ結果が等しいか表示
print(a==a2)
print(a)
print(a2)

#testcase
""" 
3
3
9 4
4 3
1 1
9 4
4 3
1 1
 """