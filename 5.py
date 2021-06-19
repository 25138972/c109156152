m = int(input("請輸入階乘值M："))
q = n = 1
while(n<=m):
    n = 1
    for i in range(1,q+1):
        n *= i
    q+=1
print("超過M為%d的最小階層N值：%d" %(m,q-1))