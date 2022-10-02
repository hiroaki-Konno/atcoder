while True:
    txt = input()
    if txt == "-":
        break
    m = int(input())
    h_list = []

    for _ in range(m):
        h_list.append(int(input()))

    for h in h_list:
        txt = txt[h:] + txt[:h]
    
    print(txt)