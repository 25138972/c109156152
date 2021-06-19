ar = input("輸入一整數序列為：").split(" ")
c = [0]*len(ar)
w = []
for i in ar:
    if i in w:
        c[ar.index(i)] += 1
    else:
        w.append(i)
q = ""
for i in c:
    if (i+1 > len(ar) / 2):
        q = ar[c.index(i)]
        break
if len(q) > 0:
    print("過半元素為：%s" %(q))
else:
    print("過半元素為：NO")