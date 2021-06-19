n = input("請輸入正整數：")
m = 0
for i in range(0,len(n)+1):
    for k in range(i+1,len(n)+1):
        isPrime = True
        s = n[i:k]
        for j in range(int(s)-1,1,-1):
            if int(s) % j == 0:
               isPrime = False
               break
        if (isPrime == True) & (int(s) > m):
            m = int(s)
if m == 0:
    print("No prime found")
else:
    print("%d" %(m))
    