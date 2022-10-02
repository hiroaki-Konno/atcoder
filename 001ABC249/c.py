nk = list(map(int, input().split()))

n=nk[0]
k=nk[1]

s =[]
st =""

max_k_count=0
k_count = 0

for _ in range(n):
    s.append(input())

#count_dic初期化
count_dic = {}
for al in "abcdefghijklmnopqrstuvwxyz":
    count_dic[al] = 0

def add_moji(c,dic):
    dic[c] += 1

def check_kcount(dic, k):
    result = 0
    for al in "abcdefghijklmnopqrstuvwxyz":
        if dic[al] == k:
            result +=1
    return result

#k個以上のsを選ぶ、k個の文字列に出てくる
#共通の文字の数を最大化

#len(s) conbination i 通りの組み合わせ

#loop = 2**n
for bit in range(1<<n):
    k_count = 0
    dic = count_dic.copy()
    for index in range(n):
        #index桁目が1ならば
        if(bit & 1<<index):
            for c in s[index]:
                add_moji(c, dic)
    for ele in dic:
        k_count = check_kcount(dic, k)
    if k_count > max_k_count:
        max_k_count = k_count

print(max_k_count)
    


