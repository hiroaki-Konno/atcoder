str = list(input())
q = int(input())
for _ in range(q):
    cmd = input().split()
    cmd[1:3] = list(map(int, cmd[1:3]))

    if cmd[0] =="print":
        print("".join(str[cmd[1]:cmd[2]+1]))
    elif cmd[0] == "reverse":
        str = str[:cmd[1]] + str[cmd[1]:cmd[2]+1][::-1] + str[cmd[2]+1:]
    elif cmd[0] == "replace":
        str[cmd[1]:cmd[2]+1] = cmd[3]