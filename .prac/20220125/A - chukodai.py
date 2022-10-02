while True:
    s = input()
    a, b =  map(int, input().split())

    a -= 1
    b -= 1

    if(b < a):
        tmp = b
        b = a
        a = b
    """ x = s[a]
    y = s[b]

    s[a] = y
    s[b] = x
    print(s) """


    print(s[:a]+s[b]+s[a+1:b]+s[a]+s[b+1:])

    #print(s[:a]+s[a]+s[a+1:b]+s[b]+s[b+1:])


