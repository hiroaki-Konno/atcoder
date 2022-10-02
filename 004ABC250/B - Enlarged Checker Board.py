N, A, B = map(int, input().split())

white = "."
black = "#"

for i in range(1,N+1):
    result = ""
    #文字列つくる
    for j in range(1,N+1):
        if (i+j) % 2 == 0:
            result += white * B
        else:
            result += black * B
    #縦列回表示
    for _ in range(A):
        print(result)