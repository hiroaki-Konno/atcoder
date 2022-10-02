""" 
行のひっくり返し方を１つに固定すると， ある列をひっくり返すかどうかは
他の列に影響を及ばさない， つまり， 列ごとに出荷できる煎餅の枚数を最大化すれば，
全体の出荷できる煎餅の枚数を最大化したことになる． 
各列において出荷できる煎餅の枚数を最大化するには， 
その列の表（と裏）の数を数え， 表が多ければひっくり返し，裏が多ければそのままにすればよい． 
全ての行のひっくり返し方に対して， この方法で出荷できる煎餅の最大枚数を求める． 
行のひっくり返し方は高々 2^10 = 1024 通りしかないので， 適切に実装すると， 
全ての採点用テストデータに対して正解できる．
 """

"""
pypyのみAC
"""

def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()

    # 整数複数個
    R, C = map(int, input().split())

    # 整数 (縦 R 横 C の行列)
    a = [list(map(int, input().split())) for _ in range(R)]

    result = 0
    for bit in range(1<<R):
        count_retsu_omote = [0]*C
        for i in range(R):
            if bit&(1<<i):
                is_reverse = 1
            else:
                is_reverse = 0
            for j in range(C):
                count_retsu_omote[j] += (a[i][j]+is_reverse) % 2 
        
        tmp_result = 0
        for omote in count_retsu_omote:
            if omote >= R/2:
                tmp_result += omote
            else:
                tmp_result += R-omote
        
        if tmp_result > result:
            result = tmp_result


    print(result)
if __name__ == '__main__':
    main()