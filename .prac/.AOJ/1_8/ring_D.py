s = input()
p = input()

def solve():
    if not p[0] in s:
        return False
    
    if p in s:
        return True

    for i,c in enumerate(s):
        if c == p[0]:#0文字目の確認
            if p in s[i:]+s[:i]:
                return True
    return False

print("Yes") if solve() else print("No")
            
