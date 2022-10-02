def solve():
    num = input()
    if num == "0":
        return False
    nums =  map(int, list(num))
    print(sum(nums))
    return True

while solve():
    None
