ar = input("輸入N及M為：").split(" ")
n = int(ar[0])
m = int(ar[1])
if ((n != 0) & (m != 0)):
    w = [[0]*m for i in range(n)]
for i in range(n):
    print("輸入矩陣數值第%d列為：" %(i+1), end="")
    q = input().split(" ")
    for k in range(m):
        w[i][k] = q[k]
s = []
for i in range(m):
    temp = ""
    for k in range(n):
        temp += w[k][i]
    s.append(" ".join(temp))
for i in range(m):
    print("輸出矩陣數值第%d列為：%s" %(i+1,s[i]))