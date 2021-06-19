ar = input("輸入月及日為：").split(" ")
month = int(ar[0])
date = int(ar[1])
w = ["Capricorn","Aquarius","Pisces","Arics","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn"]
dates = [21,19,21,21,22,22,23,24,24,24,23,22]
if date < dates[month-1]:
    print("星座為：%s" %(w[month-1]))
else:
    print("星座為：%s" %(w[month]))