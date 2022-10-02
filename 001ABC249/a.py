input_num = list(map(int, input().split()))

a = input_num[0]
b = input_num[1]
c = input_num[2]
d = input_num[3]
e = input_num[4]
f = input_num[5]
x = input_num[6]

takahasi = (x //(a+c)) * a*b
if (x % (a+c)) < a:
    takahasi += (x % (a+c)) * b
else :
    takahasi += a * b

aoki = (x //(d+f)) * d*e
if (x % (d+f)) < d:
    aoki += (x % (d+f)) * e
else :
    aoki += d * e

if takahasi > aoki:
    print("Takahashi")
elif takahasi == aoki:
    print("Draw ")
else:
    print("Aoki")