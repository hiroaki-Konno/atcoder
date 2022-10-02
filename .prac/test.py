n = int(input())

xys = {str(i):[int(t) for t in input().split()] for i in range(n)}
#xys = [[int(t) for t in input().split()] for i in range(n)]

print('0' in {'0': [9, 4], '1': [4, 3], '2': [1, 1], '3': [4, 2], '4': [2, 4], '5': [5, 8], '6': [4, 0], '7': [5, 3], '8': [0, 5], '9': [5, 2]})
