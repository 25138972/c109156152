w = int(input("輸入第一行正整數為："))
s = input("第二行中數列中的數字為：").split(" ")
ar = []
ch = [0]*w
q = 0
for i in s:
    ar.append(int(i))
for i in ar:
    for k in ar:
        if i == k:
            ch[q] += 1
    q += 1
m = 0
for i in ch:
    if (i != 1) & (i>m):
        m = i
if m == 0:
    print("每個數字剛好只出現1次")
else:
    print("最大出現次數的數字為：%d" %(ar[ch.index(max(ch))]))
    print("出現次數為：%d" %(max(ch)))