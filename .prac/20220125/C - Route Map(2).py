n, m = map(int, input().split())

local = input().split()
rapid = input().split()


""" i = 0
for t in rapid:
    #i = j
    for s in local[i:]:
        i += 1
        if (t == s):
            print("Yes")
            break
        else:
            print("No") """

i = 0
j = 0
for s in local:
    t = rapid[j]

    if (t == s):
        print("Yes")
        j += 1
    else:
        print("No")