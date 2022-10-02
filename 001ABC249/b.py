input_s = input()

tmp = []

#大文字小文字の確認
if not (input_s.islower() or input_s.isupper()) == False:
    print("No")
    quit()

#重複の確認
for i in input_s:
    if i in tmp:
        print("No")
        quit()
    tmp.append(i)

print("Yes")