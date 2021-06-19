s = input("輸入值為：").split(",")
s2 = list(s)
m1 = ""
m2 = ""
for i in range(0,len(s)):
    m1 += max(s)
    s.remove(max(s))
for i in range(0,len(s2)):
    m2 += min(s2)
    s2.remove(min(s2))
print("最大值數列與最小值數列差值為：%d" %(int(m1)-int(m2)))