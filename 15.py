s = list(input("輸入一組四位數字為："))
for i in range(4):
    s[i] = (int(s[i]) + 7) % 10
s[0],s[2] = s[2],s[0]
s[1],s[3] = s[3],s[1]
for i in range(4):
    s[i] = str(s[i])
print("輸出加密後的數字為：%s" %("".join(s)))