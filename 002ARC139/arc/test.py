n = int(input())
t = map(int, input().split())


result = 0
prev_ctz = 0 #prev T i-1
max_ctz = 0

def ctz_ti(result):
    ctz = 0
    for c in bin(result)[::-1]:
        if not c=='0':
            break
        ctz += 1
    return ctz
c=0
for t_i in t:
    #前の方が0が並んでる→指定されたctzの数字をor結合
    if prev_ctz > t_i:
        result += 1<<t_i
    
    else:
        while ctz_ti(result) != t_i:
            ctz_i = ctz_ti(result)
            result += 1<< ctz_i
            if ctz_i > t_i:
                result += 1<<t_i
    prev_result = result
    prev_ctz = t_i
    c+=1
    print(c, t_i, result)



print(result)