S = input()
result = 0

tmp = 0
for i in range(len(S)):
    if S[i] in "ACGT":
        tmp += 1
    else:
        tmp = 0
    result = max(result, tmp)

print(result)