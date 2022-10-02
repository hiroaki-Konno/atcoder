def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    # 整数複数個
    abc = list(map(int, input().split()))
    b = abc[1]
    abc.sort()

    if b==abc[1]:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()