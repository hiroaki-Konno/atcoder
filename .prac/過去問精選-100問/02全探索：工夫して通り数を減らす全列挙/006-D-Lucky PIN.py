""" 
3桁を指定するのはO(N3)かかってしまう。
だが、答えの組み合わせに注目してみると、10^3通りある。
これなら全探索できるので、10^3通りで作れるかどうか試してみる。
全ての文字について、次にある文字が出てくる最近の添字を覚えておく。
すると、先頭から3つの数を貪欲に探していくのをO(1)できる。
自分はこのへんはライブラリにしてるので、貼るだけ。
 """

N = int(input())
S = input()

""" 
#TLE祭り
password = set()
for i, si in enumerate(S[:N-2]):
    for j, sj in zip(range(i+1,N),S[i+1:N-1]):
        for sk in S[j+1:]:
            password.add(si+sj+sk)
 """

#pypyだとどうにか通った
cnt = 0

for i in range(0,1000):#0~999
    c = [i//100, (i//10)%10, i%10] #三桁のパスワードを桁ごとリストに
    f = 0
    for j in range(N):#N桁のラッキーナンバーに対してチェック
        if int(S[j]) == c[f]:
            f += 1
        if f==3:
            break
    if f==3:
        cnt += 1

print(cnt)