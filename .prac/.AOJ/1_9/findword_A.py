W = input()
T = []
while True:
    s = input()
    if s == "END_OF_TEXT":
        break
    T.append(list(s.lower().split()))

count = 0

for sentence in T:
    for s in sentence:
        if W == s:
            count += 1

#print("w", W)
#print("t", T)
print(count)