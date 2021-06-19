n = int(input())
s = 0
ns = 0
for i in range(1,n+1):
    if i <= 120:
        s += 2.1
        ns += 2.1
    elif (i<=330) & (i>120):
        s += 3.02
        ns += 2.68
    elif (i<=500) & (i>330):
        s += 4.39
        ns += 3.61
    elif (i<=700) & (i>500):
        s += 4.97
        ns += 4.01
    else:
        s += 5.63
        ns += 4.5
print("Summer months:%0.2f" %(s))
print("Non-Summer months:%0.2f" %(ns))