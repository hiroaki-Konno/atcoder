from os import curdir


count_dic = {}
for al in "abcdefghijklmnopqrstuvwxyz":
    count_dic[al] = 0

count_dic["c"] += 1
print(count_dic)
""" for ele in count_dic:
    print(ele) """

def check_kcount(dic, k, k_count):
    for al in "abcdefghijklmnopqrstuvwxyz":
        if dic[al] == k:
            k_count +=1
    
a=0
check_kcount(count_dic, 1, a)

print(a)