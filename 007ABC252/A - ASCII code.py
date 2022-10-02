def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    
    # 整数 1 つ
    N = int(input())

    print(chr(N))

if __name__ == '__main__':
    main()