n = int(input())
taba = list(map(int, input().split()))

is4n = [0]*(n+1)
is4n[0] = 4

for card in taba:
    is4n[card] += 1

for i, num in enumerate(is4n):
    if (num!= 4):
        print(i)