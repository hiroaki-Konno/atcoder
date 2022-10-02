A, B, C, X, Y = map(int, input().split())

if A+B <= 2*C:
    result = A*X + B*Y
else:
    result = 2*C*max(X, Y)
    if X < Y:
        tmp = 2*C*X + B*(Y-X)
    else:
        tmp = 2*C*Y + A*(X-Y)
    
    if result > tmp:
        result = tmp

print(result)