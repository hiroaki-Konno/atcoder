import string
result = list(map(list, list(string.ascii_lowercase)))
alp = string.ascii_lowercase
for i in range(len(result)):
    result[i].append(0)

while True:
    try:
        s = input().lower()
    except:
        break

    for c in s:
        if c in alp:
            result[alp.index(c)][1] += 1


    
for n in range(len(result)):
    print("{0} : {1}".format(alp[n], result[n][1]))
