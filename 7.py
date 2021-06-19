s = input("輸入月租費型式及通話時間為：").split(",")
w = int(s[0])
q = int(s[1])
if w == 186:
    q *= 0.09
    if q > 186:
        if q < 186*2:
            q *= 0.8
        else:
            q *= 0.9
    else:
        q = 186
elif w == 386:
    q *= 0.08
    if q > 386:
        if q < 386*2:
            q *= 0.8
        else:
            q *= 0.7
    else:
        q = 386
elif w == 586:
    q *= 0.07
    if q > 386:
        if q < 586*2:
            q *= 0.7
        else:
            q *= 0.6
    else:
        q = 386
else:
    q *= 0.06
    if q > 986:
        if q < 986*2:
            q *= 0.6
        else:
            q *= 0.5
    else:
        q = 986
print("通話費為：%0.0f" %(q))