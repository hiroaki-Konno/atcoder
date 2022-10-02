n = int(input())

taro_point, hanako_point = 0,0

for _ in range(n):
    taro, hanako = input().split()
    if taro > hanako:
        taro_point += 3
    elif hanako > taro:
        hanako_point += 3
    else:
        hanako_point += 1
        taro_point += 1

print(taro_point, hanako_point)
