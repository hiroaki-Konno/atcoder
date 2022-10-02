import math
while True:
    n = int(input())
    if n == 0:
        break
    s_list = list(map(int, input().split()))
    avg = sum(s_list)/len(s_list)
    a2 = 0
    for s in s_list:
        a2 += (s-avg)**2
    a2 /= n

    print(math.sqrt(a2))