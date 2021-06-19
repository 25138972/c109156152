while(1):
    s = input("輸入整數數列(end結束):")
    if s == "end":
        print("結束")
        break
    w = "0"
    for i in range(len(s)):
        for k in range(i+1,len(s)):
            temp = s[i:k]
            if ((temp == temp[::-1])):
                if len(temp) > len(w):
                    w = temp
                elif ((len(temp) == len(w)) & (int(temp) < int(w))):
                    w = temp
    print(w)