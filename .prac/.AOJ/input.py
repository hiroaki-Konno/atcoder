nums = []
while (True):
    x = int(input())
    if x == 0:
        break
    nums.append(x)

for i, x in enumerate(nums):
    print("Case {i}: {x}".format(i=i, x=x))