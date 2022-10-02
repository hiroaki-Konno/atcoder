H, W = map(int, input().split())
R, C = map(int, input().split())

result = 4

if H == R:
    result -= 1
if R == 1:
    result -= 1
if W == C:
    result -= 1
if C == 1:
    result -= 1

print(result)