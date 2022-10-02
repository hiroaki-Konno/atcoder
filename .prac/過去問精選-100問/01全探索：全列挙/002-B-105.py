N = int(input())

count = 0
def is_eight(i):
    divs_count = 0
    for j in range(1,N+1,2):
        if divs_count > 8:
            return False
        if i%j == 0:
            divs_count += 1
    return divs_count == 8
        
while True:
    if N < 105:
        break
    for i in range(105, N+1):
        if i%2 == 1:
            if is_eight(i):
                count += 1
    break


print(count)