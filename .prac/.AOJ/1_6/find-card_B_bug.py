n = int(input())
cards = [[0]*13]*4
marks = ["S", "H", "C", "D"]
S = cards[0]
H = cards[1]
C = cards[2]
D = cards[3]
for _ in range(n):
    mark, rank = input().split()
    if (mark == 'S'):
        cards[0][int(rank)-1] = 1
    elif (mark == 'H'):
        H[int(rank)-1] = 1
    elif (mark == 'C'):
        C[int(rank)-1] = 1
    elif (mark == 'D'):
        D[int(rank)-1] = 1

for mark in range(4):
    for rank in range(13):
        if cards[mark][rank] == 0:
            print(marks[mark], rank+1)
print(cards)