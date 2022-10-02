def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()

    # 整数複数個
    N, A, B = map(int, input().split())

    result = N * (N+1) //2
    tyoufuku = 0
    """ for i in range(A, N+1, A):
        result -= i """
    result -= (A + N//A*A) * (N//A) //2
    """ for i in range(B, N+1, B):
        result -= i """
    result -= (B + N//B*B) * (N//B) //2

    
    def gcd(a, b):
        r = a%b
        while (r!=0):
            a = b
            b = r
            r = a%b
        return b
    GCD = gcd(A, B)
    LCM = A*B//GCD
    for i in range(LCM, N+1, LCM):
        tyoufuku += i
    #print("t", tyoufuku)
    
    tmp = (LCM + (N//LCM)*LCM) * (N//LCM) //2
    result += tmp
    #print("i", tmp)
    
    
    #result += tyoufuku
    print(result)

if __name__ == '__main__':
    main()